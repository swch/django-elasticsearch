#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

VERSION = (0, 1, 0)

__version__ = ".".join(map(str, VERSION[0:3])) + "".join(VERSION[3:])
__author__ = "Alberto Paro"
__contact__ = "alberto.paro@gmail.com"
__homepage__ = "http://github.com/aparo/django-elasticsearch/"
__docformat__ = "restructuredtext"

from django.conf import settings

if not "django_elasticsearch" in settings.INSTALLED_APPS:
    if isinstance(settings.INSTALLED_APPS, tuple):
        settings.INSTALLED_APPS = ('django_elasticsearch',) + settings.INSTALLED_APPS
    else:
        settings.INSTALLED_APPS.insert(0, "django_elasticsearch")