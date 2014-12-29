# -*- coding: utf-8 -*-

from django.conf import settings
from debug_toolbar.panels import Panel

import copy
import requests
import functools
try:
    from requests_futures.sessions import FuturesSession
except Exception as e:
    print("Impossible to load requests_futures, %(e)s" % locals())
    pass

calls = []

_original_methods = dict([(method, getattr(requests, method)) for method in ["get", "post", "head", "put", "delete", "options"]])


@functools.wraps(_original_methods["get"])
def _get(url, *args, **kwargs):
    calls.append(_original_methods["get"](url, *args, **kwargs))
    return calls[-1]


@functools.wraps(_original_methods["post"])
def _post(url, *args, **kwargs):
    calls.append(_original_methods["post"](url, *args, **kwargs))
    return calls[-1]


@functools.wraps(_original_methods["put"])
def _put(url, *args, **kwargs):
    calls.append(_original_methods["put"](url, *args, **kwargs))
    return calls[-1]


@functools.wraps(_original_methods["head"])
def _head(url, *args, **kwargs):
    calls.append(_original_methods["head"](url, *args, **kwargs))
    return calls[-1]


@functools.wraps(_original_methods["delete"])
def _delete(url, *args, **kwargs):
    calls.append(_original_methods["delete"](url, *args, **kwargs))
    return calls[-1]


@functools.wraps(_original_methods["options"])
def _options(url, *args, **kwargs):
    calls.append(_original_methods["options"](url, *args, **kwargs))
    return calls[-1]

requests.get = _get
requests.post = _post
requests.head = _head
requests.put = _put
requests.delete = _delete
requests.options = _options

future_calls = []
if "FuturesSession" in locals():
    _original_methods_futures = dict([(method, getattr(FuturesSession, method)) for method in ["get", "post", "head", "put", "delete", "options"]])

    @functools.wraps(_original_methods_futures["get"])
    def _get_futures(url, *args, **kwargs):
        future_calls.append(_original_methods_futures["get"](url, *args, **kwargs))
        return future_calls[-1]

    @functools.wraps(_original_methods_futures["post"])
    def _post_futures(url, *args, **kwargs):
        future_calls.append(_original_methods_futures["post"](url, *args, **kwargs))
        return future_calls[-1]

    @functools.wraps(_original_methods_futures["put"])
    def _put_futures(url, *args, **kwargs):
        future_calls.append(_original_methods_futures["put"](url, *args, **kwargs))
        return future_calls[-1]

    @functools.wraps(_original_methods_futures["delete"])
    def _delete_futures(url, *args, **kwargs):
        future_calls.append(_original_methods_futures["delete"](url, *args, **kwargs))
        return future_calls[-1]

    @functools.wraps(_original_methods_futures["head"])
    def _head_futures(url, *args, **kwargs):
        future_calls.append(_original_methods_futures["head"](url, *args, **kwargs))
        return future_calls[-1]

    @functools.wraps(_original_methods_futures["options"])
    def _options_futures(url, *args, **kwargs):
        future_calls.append(_original_methods_futures["options"](url, *args, **kwargs))
        return future_calls[-1]

    FuturesSession.get = _get_futures
    FuturesSession.post = _post_futures
    FuturesSession.put = _put_futures
    FuturesSession.delete = _delete_futures
    FuturesSession.head = _head_futures
    FuturesSession.options = _options_futures


def _total_seconds(td):
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) * 1e-6


class RequestsDebugPanel(Panel):
    """
    Panel that displays queries made by Requests backends.
    """
    name = 'Requests'
    template = 'requests_panel/requests_panel.html'
    has_content = True

    def __init__(self, *args, **kwargs):
        super(RequestsDebugPanel, self).__init__(*args, **kwargs)
        self.queries = []

    def _get_query_count(self):
        return

    def nav_title(self):
        return 'Requests Queries'

    def nav_subtitle(self):
        return "%s queries in %.2fs" % (len(self.queries), sum([_total_seconds(q.elapsed) for q in self.queries]))

    def url(self):
        return ''

    def title(self):
        return self.nav_title()

    def get_context(self):
        global calls, future_calls
        self.queries = copy.deepcopy(calls) + [copy.deepcopy(c.result()) for c in future_calls if not c.running()]

        for q in self.queries:
            q.total_seconds = _total_seconds(q.elapsed)
        calls = []
        future_calls = []

        return {
            'queries': self.queries,
            'debug': getattr(settings, 'DEBUG', False),
        }

    def process_response(self, request, response):
        if hasattr(self, 'record_stats'):
            self.record_stats(self.get_context())
