from django.db import models
from django.contrib.auth.models import User

from cased_django import CasedModelEvent


class Creator(models.Model):
    pass


class Post(models.Model, CasedModelEvent):
    """
    A test model with no Cased-specific additions
    """

    user = User()
    body = models.TextField()


class Comment(models.Model, CasedModelEvent):
    """
    A test model with a shortcut cased_actor and additional cased_payload
    """

    body = models.TextField()

    # To be used as a custom actor attr
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    # Shortcut for sending the actor
    @property
    def cased_actor(self):
        return self.creator

    # Custom additional data to send to Cased
    @property
    def cased_payload(self):
        return {"country": "Austria", "is_staff": False}


class Photo(models.Model, CasedModelEvent):
    """
    A test model with custom action
    """

    user = User()
    body = models.TextField()

    @property
    def cased_payload(self):
        return {"action": "custom.event"}
