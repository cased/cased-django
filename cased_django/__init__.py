from threading import local

version = "0.6.0"

cased_thread_locals = local()


def get_ip_address():
    return getattr(cased_thread_locals, "ip_address", None)


def set_ip_address(ip):
    setattr(cased_thread_locals, "ip_address", ip)


from cased_django import conf
from .client import cased_client
from .middleware import CasedIpMiddleware
from .cased_model_event import CasedModelEvent
from .event_manager import EventManager
