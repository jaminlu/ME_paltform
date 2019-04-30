# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,get_object_or_404
from users.forms import LoginForm, UserForm,RegistrationForm,ProfieForm,ChangePwdForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from ManageEngine.api.app_func import alert, admin_required
from django.db import transaction
from django.contrib import messages
from users.models import UserProfile
# Create your views here.
import datetime


@login_required(login_url="/login")
def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    print("start index")
    username = request.user
    nowtime = datetime.datetime.now()
    return render(request, 'users/index.html', locals())


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
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
    return redirect('/login')

def register(request):
    if request.method == 'POST':
        print("register begin")
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = User.objects.create_user(username=username, password=password, email=email)

            user_profile = UserProfile(user=user)
            user_profile.save()
            print('register success!!')
            return redirect('/login.html')

    else:
        form = RegistrationForm
    return render(request, 'users/register.html',{'form':form})

@login_required()
def profile(request):
    current_user = request.user
    user = get_object_or_404(User,pk=current_user.id)
    print(user)
    return render(request, 'users/profile.html', {'user': user})

@login_required()
def profile_update(request):
    print('enter profile_update')
    current_user = request.user
    print(current_user)
    id = current_user.id
    print(id)
    user = get_object_or_404(User, pk=id)
    user_profile = get_object_or_404(UserProfile,user_id=id)
    print("sss %s" % user_profile)
    if request.method == 'POST':
        form = ProfieForm(request.POST)

        if form.is_valid():

            user_profile.dep = form.cleaned_data['dep']
            user_profile.telephone = form.cleaned_data['telephone']
            print(user_profile)
            user_profile.save()

            return render(request,'users/profile.html', {'user':user})
    else:
        default_data = {'first_name': user.first_name, 'last_name':user.last_name, 'dep':user_profile.dep, 'telephone':user_profile.dep}
        form = ProfieForm(default_data)
        return render(request,'users/profile_update.html', {'form':form, 'user':user})

@login_required()
def get_user_id(request):
    try:
        return request.user.id
    except:
        return None

@login_required()
def changepwd(request):
    id = get_user_id(request)
    user = get_object_or_404(User, pk=id)

    if request.method == "POST":
        form = ChangePwdForm(request.POST)
        print(form)
        if form.is_valid():
            password = form.cleaned_data['old_password']
            username = user.username
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect("/login.html")
            else:
                return render(request, 'users/changepwd.html',{'form':form, 'user':user, 'message':'Old password is wrong, Try again'})
    else:
        form = ChangePwdForm()
    return render(request, 'users/changepwd.html',{'form':form, 'user':user})


@login_required()
def user_list(request):
    users1 = User.objects.all()
    users = User.objects.all().order_by('id')
    # phone = Profile.objects.filter(id__gt=0)
    return render(request, 'users/users_list.html', {'users': users})


def load_profile(user):
    try:
        return user.profile
    except:
        profile = Profile.objects.create(user=user)
        return profile

'''
@admin_required()
@transaction.atomic
def user_update(request, id):
    user = User.objects.filter(id=id)
    username = User.objects.get(id=id)
    profile = load_profile(username)
    print('enter')
    user_form = UserForm(request.POST, instance=username)  # print the user of operate
    profile_form = ProfileForm(request.POST, instance=profile)
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
'''
def perm_deny(request):
    return render(request, 'perm_deny.html', locals())