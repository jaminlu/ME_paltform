# Create your views here.

from django.contrib.auth.decorators import login_required
from assets import models
from assets.forms import IdcForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render

#@login_required
def assetinfo(request):
    print("assetsinfo")
    the_assets = models.Assets.objects.all()
    return render(request,'assets/asset_info.html',locals())
    print(the_assets)

def idcdetail(request,func):
    if request.method == 'GET':
        print(type(func))
        obj = models.IDC.objects.get(id=func)
        return render(request,'assets/asset_detail.html', locals())


def page_not_found(request):
    return render_to_response("404.html")

def index(request):
    print("index")
    return render_to_response("404.html")

#展示机房信息
def idcinfo(request):
    print("idc info'")
    idc_info = models.IDC.objects.all()
    #for i in idc_info:
    #    print(i.name)
    #print(idc_info)
    return render(request,'assets/idc_info.html',locals())

#新增机房
def idcadd(request):
    print("add idcinfo")
    form=IdcForm()
    if request.method == "POST":
        form = IdcForm(request.POST)
        if form.is_valid():
            #form_data = form.cleaned_data
            #print(form_data)
            #new_idc_obj = models.IDC(**form_data)
            #new_idc_obj.save()
            form.save()
            return HttpResponseRedirect('assetinfo/')
    else:
        form=IdcForm()
    print("通过ajax传参数过来，然后更新model")
    return render(request,'assets/idc_add.html',locals())

#机房信息编辑
def idcinfo_edit(request):
    return
