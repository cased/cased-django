#!/usr/bin/env python
import os
import sys
from django.test.utils import get_runner
from django.conf import settings


testdir = os.path.join(os.path.dirname(__file__), "cased_django", "tests")

sys.path.insert(0, testdir)


def run():
    os.environ["DJANGO_SETTINGS_MODULE"] = "test_app.settings"

    import django

    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(["test_app"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    run()
