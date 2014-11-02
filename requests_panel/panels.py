from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from debug_toolbar.panels import Panel

import copy
import requests
import functools

_original_methods = dict([(method, getattr(requests, method)) for method in ["get", "post", "head", "put", "delete", "options"]])

calls = []

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
        global calls
        self.queries = copy.deepcopy(calls)
        for q in self.queries:
            q.total_seconds = _total_seconds(q.elapsed)
        calls = []

        return {
            'queries': self.queries,
            'debug': getattr(settings, 'DEBUG', False),
        }

    def process_response(self, request, response):
        if hasattr(self, 'record_stats'):
            self.record_stats(self.get_context())
