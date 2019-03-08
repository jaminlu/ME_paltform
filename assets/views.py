# Create your views here.

from django.contrib.auth.decorators import login_required
from assets import models
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render

#@login_required
def assetinfo(request):
    print("assetsinfo")
    the_assets = models.Assets.objects.all()
    return render(request,'assets/asset_info.html',locals())
    print(the_assets)


def page_not_found(request):
    return render_to_response("404.html")

def index(request):
    print("index")
    return render_to_response("404.html")

#展示机房信息
def idcinfo(request):
    print("idc info'")
    idc_info = models.IDC.objects.all()

    return render(request,'assets/idc_info.html',locals())

#新增机房
def idcadd(request):
    print("add idcinfo")
    print("通过ajax传参数过来，然后更新model")
    return None

#机房信息编辑
def idcinfo_edit(request):
    return
