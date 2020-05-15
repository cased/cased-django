try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

from cased_django import set_ip_address


class CasedIpMiddleware:
    def __init__(self, get_response):
        set_ip_address(None)
        self.get_response = get_response

    def _client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def __call__(self, request):
        ip = self._client_ip(request)
        set_ip_address(ip)
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        set_ip_address(None)
        return None
