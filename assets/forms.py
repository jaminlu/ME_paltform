#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import *
from assets.models import Assets, IDC
import datetime


class IdcForm(forms.ModelForm):
    name = forms.CharField(label=u'机房名称', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    idc_flag = forms.CharField(label=u'机房标示', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label=u'机房地址', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tel_ip = forms.CharField(label=u'电信IP', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),
                             validators=[validate_ipv4_address])
    uni_ip = forms.CharField(label=u'联通IP',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validate_ipv4_address])
    mob_ip = forms.CharField(label=u'移动IP',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validate_ipv4_address])
    dns_ip = forms.CharField(label=u'DNS IP',required=True,widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validate_ipv4_address])
    email = forms.EmailField(label=u'邮箱地址', required=False, widget=forms.TextInput(attrs={'class':'form-control'}), validators=[validate_email])
    comment = forms.CharField(label=u'备注',required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=IDC
        fields=('name','idc_flag','address','tel_ip','uni_ip','mob_ip','dns_ip','email','comment')

    #def __init__(self,*args, **kwargs):
    #    super(IdcForm,self).__init__(*args, **kwargs)
    #    self.fields['add_time']="2018-03-09"
    #    self.fields['mod_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')




