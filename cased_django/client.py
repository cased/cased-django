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
    redact_before_publishing,
    clear_context_after_publishing,
)


def get_cased_client():
    cased.publish_key = publish_key
    cased.api_base = api_base
    cased.publish_base = publish_base
    cased.disable_publishing = disable_publishing
    cased.reliability_backend = reliability_backend
    cased.sensitive_data_handlers = sensitive_data_handlers
    cased.sensitive_fields = sensitive_fields
    cased.log_level = log_level
    cased.redact_before_publishing = redact_before_publishing
    cased.clear_context_after_publishing = clear_context_after_publishing
    return cased


cased_client = get_cased_client()
