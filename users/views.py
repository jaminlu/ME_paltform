# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from users.forms import LoginForm, UserForm,RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from ManageEngine.api.app_func import alert, admin_required
from django.db import transaction
from django.contrib import messages
from users.models import UserProfile
# Create your views here.


@login_required(login_url="/login.html")
def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    print("start index")
    return render(request, 'users/index.html', locals())


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        print("ffff")
        return render(request, 'users/login.html', {'form': form})
    if request.method=="POST":
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(password)
            user = authenticate(username=username, password= password)
            print(user)
            if user is not None and user.is_active:
                login(request,user)
                #print("request_session: %s" % request.session)
                request.session['is_login']=True

                login_ip = request.META['REMOTE_ADDR']
                print("auth success")
                return redirect('/index')
            else:
                return render(request, 'users/login.html', {'form': form})
        else:
            return render(request,'users/login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = User.objects.create_user(username=username, password=password, email=email)

            user_profile = UserProfile(user=user)
            user_profile.save()
            return render(request,'users/login.html')

    else:
        form = RegistrationForm
    return render(request, 'users/register.html',{'form':form})

@login_required()
def profile(request):
    username = request.user
    return render(request, 'hello.html', locals())


@login_required()
def user_list(request):
    users1 = User.objects.all()
    print(users1)
    users = User.objects.all().order_by('id')
    print(users)
    # phone = Profile.objects.filter(id__gt=0)
    return render(request, 'users/users_list.html', {'users': users})


def load_profile(user):
    try:
        return user.profile
    except:
        profile = Profile.objects.create(user=user)
        return profile


@admin_required()
@transaction.atomic
def user_update(request, id):
    print(id)
    user = User.objects.filter(id=id)
    username = User.objects.get(id=id)
    profile = load_profile(username)
    print('enter')
    user_form = UserForm(request.POST, instance=username)  # print the user of operate
    print(user_form)
    profile_form = ProfileForm(request.POST, instance=profile)
    print(profile_form)
    if request.method == 'POST':
        print(user_form)
        print(profile_form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            # alert(request, u'user %d added' % the_user.username)
            return HttpResponseRedirect('/users/user_list')
        else:
            print('ooo')
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'users/user_update.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        return render(request, 'users/user_update.html', locals())

def perm_deny(request):
    return render(request, 'perm_deny.html', locals())