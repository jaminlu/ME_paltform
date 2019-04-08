# Create your views here.

from django.contrib.auth.decorators import login_required
from idc import models
from idc.forms import IdcForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from idc.models import IDC


def idcdetail(request, func):
    if request.method == 'GET':
        print(type(func))
        obj = models.IDC.objects.get(id=func)
        print("enter idcdetail")
        return render(request, 'idc/../templates/assets/asset_detail.html', locals())


def page_not_found(request):
    return render_to_response("404.html")


def index(request):
    print("index")
    return render_to_response("404.html")


# 展示机房信息
def idcinfo(request):
    print("idc info'")
    idc_info = models.IDC.objects.all()
    for i in idc_info:
        print(i.name)
    print(idc_info)
    return render(request, 'idc/idc_info.html', locals())


# 新增机房
def idcadd(request):
    form = IdcForm()
    if request.method == "POST":
        form = IdcForm(request.POST)
        if form.is_valid():
            # form_data = form.cleaned_data
            # print(form_data)
            # new_idc_obj = models.IDC(**form_data)
            # new_idc_obj.save()
            form.save()
            return HttpResponseRedirect('idcinfo/')
    else:
        form = IdcForm()
    return render(request, 'idc/idc_add.html', locals())


# 编辑机房信息
def idcedit(request):
    print("idc edit")
    print(id)
    return None


# 机房信息编辑
def idcinfo_edit(request):
    id = request.POST.get('id')
    idc_info = IDC.objects.get(id=int(id))
    print(idc_info)
    if request.method == 'POST':
        print("idc_edit")
        print("id is %s" % id)
        form = IdcForm(request.POST,instance=idc_info)
        if form.is_valid():
            print('post success')
            form.save()
            return HttpResponseRedirect('idcinfo/')
    else:
        form = IdcForm()

    return render(request,'idc/idc_info.html',locals())
