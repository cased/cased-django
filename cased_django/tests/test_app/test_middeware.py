from cased_django import CasedIpMiddleware, get_ip_address, set_ip_address
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse

import unittest


def mock_response(request):
    response = HttpResponse()
    response.status_code = 200
    response.json = {"key-1": "value-1"}
    return response


class TestMiddleware(TestCase):
    def test_ip_address_is_set_automatically_in_middleware(self):
        middleware = CasedIpMiddleware(mock_response)
        request = RequestFactory().get("/")
        request.user = AnonymousUser()
        middleware(request)
        self.assertEquals(get_ip_address(), "127.0.0.1")

    def test_ip_address_can_be_returned(self):
        set_ip_address("localhost")
        self.assertEquals(get_ip_address(), "localhost")
