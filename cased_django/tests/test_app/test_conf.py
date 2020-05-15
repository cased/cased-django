from django.test import TestCase

import cased
from cased_django.conf import (
    publish_key,
    api_base,
    publish_base,
    disable_publishing,
    reliability_backend,
    sensitive_data_handlers,
    sensitive_fields,
    log_level,
    include_ip_address,
)


class CasedConfTestCase(TestCase):
    def setUp(self):
        """
        The test values are all set in the test_app.settings.py
        """
        pass

    def test_publish_key_can_be_set(self):
        self.assertEqual(publish_key, "test-key-123")

    def test_api_base_can_be_set(self):
        self.assertEqual(api_base, "https://api.example.com")

    def test_publish_base_can_be_set(self):
        self.assertEqual(publish_base, "https://publish.example.com")

    def test_disable_publishing_can_be_set(self):
        self.assertEqual(disable_publishing, True)

    def test_reliability_backend_can_be_set(self):
        self.assertEqual(reliability_backend, "redis")

    def test_log_level_can_be_set(self):
        self.assertEqual(log_level, "INFO")

    def test_include_ip_address_can_be_set(self):
        self.assertEqual(include_ip_address, True)

    def test_sensitive_fields_can_be_set(self):
        self.assertEqual(sensitive_fields, {"email_address"})

    def test_sensitive_data_handlers_default_to_empty_list(self):
        self.assertEqual(sensitive_data_handlers, [])
