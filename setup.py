import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


setup(
    name="cased-django",
    version="0.6.0",
    description="Django integration for Cased",
    long_description="Django integration for Cased",
    author="Cased",
    author_email="support@cased.com",
    url="https://github.com/cased/cased-django",
    license="Apache",
    keywords="cased api",
    packages=["cased_django"],
    install_requires=["cased>=0.3.5"],
    zip_safe=False,
    python_requires=">3.5",
    project_urls={
        "Bug Tracker": "https://github.com/cased/cased-django/issues",
        "Source Code": "https://github.com/cased/cased-django",
    },
)
