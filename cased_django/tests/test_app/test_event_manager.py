from django.test import TestCase
from unittest import mock
import cased

from cased_django import CasedModelEvent, EventManager
from .models import Post, Comment, Creator

from django.contrib.auth.models import User

from cased_django.event_manager import event_save


class TestEventManager(TestCase):
    def setUp(self):
        Post.objects.all().delete()
        Comment.objects.all().delete()

    def test_event_manager_publishes_on_model_save(self):
        with mock.patch("cased.Event.publish") as _:
            post = Post()
            post.user = User(id=1)
            post.save()
            cased.Event.publish.assert_called_with(
                {"action": "post.create", "location": None}
            )

    def test_event_manager_publishes_on_model_update(self):
        with mock.patch("cased.Event.publish") as _:
            post = Post()
            post.user = User(id=2)
            post.save()
            cased.Event.publish.assert_called_with(
                {"action": "post.create", "location": None}
            )

            # update it
            post.body = "Test data"
            post.save()
            cased.Event.publish.assert_called_with(
                {"action": "post.update", "location": None}
            )

    def test_event_manager_publishes_on_model_delete(self):
        with mock.patch("cased.Event.publish") as _:
            post = Post()
            post.user = User(id=2)

            post.save()
            cased.Event.publish.assert_called_with(
                {"action": "post.create", "location": None}
            )

            post.delete()
            cased.Event.publish.assert_called_with(
                {"action": "post.delete", "location": None}
            )

    def test_event_manager_publishes_on_model_save_with_payload(self):
        with mock.patch("cased.Event.publish") as _:
            creator = Creator()
            creator.id = 2
            creator.save()

            comment = Comment()
            comment.creator = creator
            comment.save()
            cased.Event.publish.assert_called_with(
                {
                    "action": "comment.create",
                    "country": "Austria",
                    "is_staff": False,
                    "actor": "Creator;2",
                    "location": None,
                }
            )
