# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from ManageEngine.api import *
from django.shortcuts import render_to_response,render
import datetime


@login_required()
def index(request):
    content = u'welcome to AutoOps'
    username = request.user
    print(username)
    nowtime = datetime.datetime.now()
    print('index')

    #return render_to_response('hello.html')
    return render(request, 'index.html',locals())
    # return render_to_response('users/login.html')


def perm_deny(request):
    return render(request, 'perm_deny.html', locals())
