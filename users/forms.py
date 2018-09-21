# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from users.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': u'username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': u'password'}))


class AddUserForm(forms.ModelForm):
    username = forms.CharField(label=u'username', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=u'password', required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(label=u'phonenumber', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label=u'email', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('username', 'password','tel','dep','email')
