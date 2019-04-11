#!/usr/bin/env python

from __future__ import absolute_import,unicode_literals
import os
from celery import Celery, platforms

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ManageEngine.settings')

app = Celery('ManageEngine')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))