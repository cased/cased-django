import cased
from django.conf import settings

publish_key = getattr(settings, "CASED_PUBLISH_KEY", None)

log_level = getattr(settings, "CASED_LOG_LEVEL", None)

api_base = getattr(settings, "CASED_API_BASE", cased.api_base)
publish_base = getattr(settings, "CASED_PUBLISH_BASE", cased.publish_base)

disable_publishing = getattr(settings, "CASED_DISABLE_PUBLISHING", False)
include_ip_address = getattr(settings, "CASED_INCLUDE_IP_ADDRESS", False)

reliability_backend = getattr(settings, "CASED_RELIABILITY_BACKEND", None)
sensitive_data_handlers = getattr(settings, "CASED_SENSITIVE_DATA_HANDLERS", [])
sensitive_fields = getattr(settings, "CASED_SENSITIVE_FIELDS", set())

redact_before_publishing = getattr(settings, "CASED_REDACT_BEFORE_PUBLISHING", False)

clear_context_after_publishing = getattr(
    settings, "CASED_CLEAR_CONTEXT_AFTER_PUBLISHING", False
)
