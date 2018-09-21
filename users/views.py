# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import Group, User
from django.shortcuts import render, render_to_response
from users.forms import LoginForm, AddUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ManageEngine.api.app_func import alert,admin_required
# Create your views here.
import sys


def login(request):
    form = LoginForm()
    error = ''
    if request.user.is_authenticated:
        print("authoried")
        return HttpResponseRedirect("index/")
    if request.method == 'GET':
        print("ffff")
        return render(request, 'users/login.html', {'form':form})
    else:
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print("sss"+ password)
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print('login')
                    return HttpResponseRedirect(request.session.get('pre_url', '/'))
                else:
                    error = u'user has not activate'
            else:
                error = u'username or password may be wrong'
        else:
            error = u'username or password may be wrong'
    return render(request, 'users/login.html', {'form': form})


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/users/login')


@login_required()
def profile(request):
    username = request.user
    print(username)
    return render(request, 'hello.html',locals())

@login_required()
def user_list(request):
    users = User.objects.filter(id__gt=0)
    return render(request, 'users/users_list.html', locals())


@admin_required()
def user_add(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        print('post')
        if form.is_valid():
            form.save()
            the_user = User.objects.get(username=request.POST.get('username'))
            the_user.set_password(request.POST.get('password'))
            the_user.save()

            alert(request, u'user %d added' % the_user.username)
            print('add')
            return HttpResponseRedirect('/user_add')
        else:
            print('ooo')
            form = AddUserForm()
    return render(request, 'users/user_add.html', locals())


