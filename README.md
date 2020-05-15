# cased-django

`cased-django` is the official Django SDK for [Cased](https://cased.com), a web service for adding audit trails to any application in minutes. This Django app also provides lower-level access to the [`cased-python`](https://github.com/cased/cased-python) client library if you need it.

![cased-django](https://github.com/cased/cased-django/workflows/cased-django/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

| Contents                       |
| :----------------------------- |
| [Installation](##installation) |
| [How To Guide](##usage-guide)  |
| [Contributing](##contributing) |

# Installation

Add `cased-django` as a dependency:

```
pipenv install cased_django
```

Add `cased_django` to `INSTALLED_APPS` in your Django settings file. You'll need to set a `CASED_API_KEY` variable as well. We strongly recommend using environmental variables instead of hard-coding the key in your settings file.

```python
import os

INSTALLED_APPS = [
    ...
    'cased_django'
]

CASED_PUBLISH_KEY = os.getenv["CASED_PUBLISH_KEY"]
```

## How To Guide

You can use `cased-django` to automatically send `create`, `update`, and `delete` events to Cased by inheriting from `CasedModelEvent`. For example, with a `Comment` model:

```python

from cased_django import CasedModelEvent

class Comment(models.Model, CasedModelEvent):
    ...
```

Events will be now sent to Cased any time `save()` or `delete()` is called on that model.

### Event Structure

`cased-django` creates `dict` objects (which are serialized to JSON) that look like this:

```python
{
    "action": "comment.create"
    ...
}
```

Action names are automatically generated based on model name.

You will want to add additional data to this. In your model, just set a `cased_payload` property to do that. For example:

```python
class Comment(models.Model, CasedModelEvent):
    ...

    @property
    def cased_payload(self):
        return {"actor": self.user.name, "body": self.body}
```

and

```python
{
    "action": "comment.create"
    "actor": "some-user",
    "body": "A good comment"
}
```

will be sent.

### Actor Shortcut

A common need in audit logging is to include the _actor_ of an event. Provide `cased_actor` in your model, and a structured `actor` will be added your payload. `cased_actor` must return a model instance.

```python
class Comment(models.Model, CasedModelEvent):
    ...

    @property
    def cased_actor(self):
        return self.creator
```

This will send a payload based on the `pk` of that `creator` instance:

```python
{
    "action": "comment.create"
    "actor": "Creator;1"
}
```

Future additions to `cased_django` will provide similar contextual shortcuts for any model field you may want.

### Automatically Send IP addresses

Good audit logging includes IP addresses. You can automatically include IP addresses with any payload sent in a `CasedModelEvent` by setting a configuration value and adding one middleware class.

In settings.py, set:

```python
CASED_INCLUDE_IP_ADDRESS = True
```

Then add `CasedIpMiddleware` to your settings.py `MIDDLEWARE` (or `MIDDLEWARE_CLASSES` in older versions of Django)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    'cased_django.CasedIpMiddleware',
]
```

### Additional Configuration

You may want to completely prevent events from being published (for example, in testing). In `settings.py`:

```python
CASED_DISABLE_PUBLISHING = True
```

For additional configuration options see [cased-python](https://github.com/cased/cased-python):

```python
CASED_RELIABILITY_BACKEND = "redis" # or your custom class
CASED_SENSITIVE_DATA_HANDLERS = [] # Your sensitive data handlers
CASED_SENSITIVE_FIELDS = {"some_field", "another_field"} # Your sensitive fields
```

### Logging

Optionally set logging in your settings. `INFO` or `DEBUG` are valid options.

```python
CASED_LOG_LEVEL = "INFO"
```

or

```python
CASED_LOG_LEVEL = "DEBUG"
```

### Using `cased-python` directly

To use the underlying [`cased-python`](https://github.com/cased/cased-python) library directly:

```python

from cased_django import cased_client

cased_client.Event.publish({})
```

## Contributing

Contributions to this library are welcomed and a complete test suite is available.

Code formatting and linting is provided by [Black](https://black.readthedocs.io/en/stable/) and [Flake8](https://flake8.pycqa.org/en/latest/) respectively, so you may want to install them locally.
