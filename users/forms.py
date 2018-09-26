# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from users.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': u'username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': u'password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username'}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'phone', 'dep','birth_date'}

