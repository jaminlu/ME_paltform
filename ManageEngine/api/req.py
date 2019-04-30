# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.shortcuts import render


def http_success(request, msg):
    return render(request, 'success.html', locals())


def http_error(request, msg):
    return render(request, 'error.html', locals())


def request_user_id(request):
    request_user = User.objects.get(username=request.user)
    return request_user.id



