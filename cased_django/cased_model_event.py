from django.utils.text import slugify
from cased_django.conf import include_ip_address
from . import get_ip_address


class CasedModelEvent(object):
    """
    Inherit from CasedModelEvent on your models to get automatic sending of
    audit entries to Cased.
    """

    @property
    def cased_payload(self):
        """
        Override with a dict to add any data you would like to send to Cased.

        Returns a dictionary
        """
        return {}

    @property
    def cased_actor(self):
        """
        Convenience function to automatically generate an actor with a standardized
        format. Subclass this in your custom model. For example

            class MyModel(models.Model, CasedModelEvent):
                author = ....

            @property
            def cased_actor(self):
                return self.author

        Returns a model instance.
        """
        return None

    @property
    def cased_event_actor(self):
        actor = self.cased_actor
        klass_name = actor.__class__.__name__

        pk = str(actor.pk)
        return klass_name + ";" + pk

    @property
    def cased_class_name(self):
        return slugify(self.__class__.__name__)

    def cased_event_action(self, event_type):
        return self.cased_class_name + "." + event_type

    def make_cased_event(self, instance, event_type):
        cased_payload = self.cased_payload

        if self.cased_actor:
            actor = self.cased_event_actor
            cased_payload["actor"] = actor

        if include_ip_address:
            cased_payload["location"] = get_ip_address()

        action = cased_payload.pop("action", None)
        if not action:
            # Auto-generate the action
            action = self.cased_event_action(event_type)

        event = dict(action=action, **cased_payload)

        return event
