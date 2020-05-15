from django.db.models.signals import class_prepared, post_save, post_delete

from cased_django import cased_client
from cased_django import CasedModelEvent
from django.dispatch import receiver


class EventManager(object):
    @classmethod
    def publish_to_cased(cls, event):
        return cased_client.Event.publish(event)

    @classmethod
    def publish_create(cls, instance):
        event = instance.make_cased_event(instance, "create")
        return cls.publish_to_cased(event)

    @classmethod
    def publish_update(cls, instance):
        event = instance.make_cased_event(instance, "update")
        return cls.publish_to_cased(event)

    @classmethod
    def publish_delete(cls, instance):
        event = instance.make_cased_event(instance, "delete")
        return cls.publish_to_cased(event)


# Signal receivers


@receiver(class_prepared)
def bind_model(sender, **kwargs):
    """
    If the prepared class is a subclass of CasedModelEvent, then connect
    post_save and post_delete signals to it.

    Returns nothing.
    """
    if issubclass(sender, (CasedModelEvent,)):
        post_save.connect(event_save, sender=sender)
        post_delete.connect(event_delete, sender=sender)


def event_save(sender, instance, created, raw, **kwargs):
    if created:
        # new record
        return EventManager.publish_create(instance)
    else:
        # existing record
        return EventManager.publish_update(instance)


def event_delete(sender, instance, **kwargs):
    return EventManager.publish_delete(instance)
