from django.test import TestCase

from django.conf import settings
from django.contrib.auth.models import User

from .models import Post, Comment, Creator, Photo


class CasedModelEventTestCase(TestCase):
    def setUp(self):
        self.post = Post()
        self.post.id = 1
        self.post.body = "Post details"
        self.post.user = User(id=1)

        self.comment = Comment()
        self.comment.id = 10
        self.comment.body = "Comment details"
        self.comment.creator = Creator(id=1)

        self.photo = Photo()

    def test_model_has_ordinary_methods(self):
        post = self.post
        self.assertEqual(post.id, 1)
        self.assertEqual(post.body, "Post details")

    def test_model_can_generate_event_actions(self):
        post = self.post
        self.assertEqual(post.cased_event_action("create"), "post.create")

    def test_model_has_no_added_payload_data_by_default(self):
        post = self.post
        self.assertEqual(post.cased_payload, {})

    def test_model_can_return_a_class_name(self):
        post = self.post
        self.assertEqual(post.cased_class_name, "post")

    def test_model_can_make_cased_events_for_create(self):
        post = self.post
        event = post.make_cased_event(post, "create")

        expected_event = {"action": "post.create", "location": None}

        self.assertEqual(event, expected_event)

    def test_model_can_make_cased_events_for_update(self):
        post = self.post
        event = post.make_cased_event(post, "update")
        expected_event = {"action": "post.update", "location": None}
        self.assertEqual(event, expected_event)

    def test_custom_actor_be_set(self):
        comment = self.comment
        self.assertEqual(comment.cased_event_actor, "Creator;1")

    def test_payload_can_be_added(self):
        comment = self.comment
        event = comment.make_cased_event(comment, "create")
        expected_event = {
            "action": "comment.create",
            "actor": "Creator;1",
            "is_staff": False,
            "country": "Austria",
            "location": None,
        }

        self.assertEqual(event, expected_event)

    def test_action_can_be_overriden(self):
        photo = self.photo
        event = photo.make_cased_event(photo, "create")
        expected_event = {"action": "custom.event", "location": None}

        self.assertEqual(event, expected_event)
