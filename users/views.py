# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import Group, User
from django.shortcuts import render, render_to_response
from users.forms import LoginForm, ProfileForm, UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ManageEngine.api.app_func import alert,admin_required
from django.db import transaction
from users.models import Profile
from django.contrib import messages
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


def load_profile(user):
    try:
        return user.profile
    except:
        profile = Profile.objects.create(user=user)
        return profile


@admin_required()
@transaction.atomic
def user_update(request):
    profile=load_profile(request.user)
    print('enter')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)  #print the user of operate
        print(request.user)
        print("================")
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        print(user_form)
        print('11111')
        print(profile_form)
        if user_form.is_valid() and profile_form.is_valid():
            print("write")
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            #alert(request, u'user %d added' % the_user.username)
            return HttpResponseRedirect('/users/user_list')
        else:
            print('ooo')
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'users/user_update.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        return render(request, 'users/user_update.html',locals())

