# -*- coding: utf-8 -*-

import logging
import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect

from message.models import Alter
from .req import request_user_id


def alert(request, text):
    a = Alter(text=text, to_user_id=request_user_id(request))
    a.save()


def admin_required():
    def _deco(func):
        def __deco(request, *args, **kwargs):
            if not request.user.is_superuser:
                return HttpResponseRedirect('index/')
            return func(request, *args, **kwargs)

        return __deco

    return _deco
