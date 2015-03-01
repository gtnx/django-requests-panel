# -*- coding: utf-8 -*-

from django.conf import settings
from debug_toolbar.panels import Panel
from requests_wrapper import _total_seconds, retrieve_all_queries


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
        self.queries = retrieve_all_queries()

        return {
            'queries': self.queries,
            'debug': getattr(settings, 'DEBUG', False),
        }

    def process_response(self, request, response):
        if hasattr(self, 'record_stats'):
            self.record_stats(self.get_context())
