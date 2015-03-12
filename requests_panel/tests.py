# -*- coding: utf-8 -*-

import datetime
import os
import unittest
import requests
import requests_cache
from requests_wrapper import retrieve_all_queries, _total_seconds
from requests_futures.sessions import FuturesSession


class PanelsTest(unittest.TestCase):
    def setUp(self):
        requests_cache.install_cache(
            cache_name=os.path.join(os.path.dirname(__file__), "test"),
            allowable_codes=(200, 404),
            allowable_methods=('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS')
        )

    def test_all(self):
        self.assertEquals(_total_seconds(datetime.timedelta(hours=1)), 3600)
        self.assertEquals(_total_seconds(datetime.timedelta(minutes=10)), 600)
        requests.get("http://httpbin.org/get")
        requests.post("http://httpbin.org/post")
        requests.put("http://httpbin.org/put")
        requests.delete("http://httpbin.org/delete")
        requests.head("http://httpbin.org/head")
        requests.options("http://httpbin.org/options")
        
        session = FuturesSession()
        futures = []
        futures.append(session.get("http://httpbin.org/get"))
        futures.append(session.post("http://httpbin.org/post"))
        futures.append(session.put("http://httpbin.org/put"))
        futures.append(session.delete("http://httpbin.org/delete"))
        futures.append(session.head("http://httpbin.org/head"))
        futures.append(session.options("http://httpbin.org/options"))

        [f.result() for f in futures]

        queries = retrieve_all_queries()
        self.assertEqual(len(queries), 12)
        for q in queries:
            self.assertTrue(isinstance(q, requests.models.Response))
