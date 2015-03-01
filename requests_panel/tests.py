# -*- coding: utf-8 -*-

import unittest
import requests
from requests_wrapper import retrieve_all_queries
from requests_futures.sessions import FuturesSession


class PanelsTest(unittest.TestCase):
    def test_all(self):
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
            self.assertIsInstance(q, requests.models.Response)
