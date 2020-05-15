from django.test import TestCase

from cased_django import cased_client


class CasedClientTestCase(TestCase):
    def setUp(self):
        """
        The test values are all set in the test_app.settings.py
        """
        pass

    def test_cased_client_is_configured(self):
        self.assertEqual(cased_client.publish_key, "test-key-123")
        self.assertEqual(cased_client.api_base, "https://api.example.com")
        self.assertEqual(cased_client.publish_base, "https://publish.example.com")
        self.assertEqual(cased_client.disable_publishing, True)
        self.assertEqual(cased_client.reliability_backend, "redis")
        self.assertEqual(cased_client.log_level, "INFO")
        self.assertEqual(cased_client.sensitive_fields, {"email_address"})
        self.assertEqual(cased_client.sensitive_data_handlers, [])
