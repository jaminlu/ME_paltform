# Create your views here.

from django.contrib.auth.decorators import login_required
from idc import models
from idc.forms import IdcForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render



def idcdetail(request,func):
    if request.method == 'GET':
        print(type(func))
        obj = models.IDC.objects.get(id=func)
        return render(request, 'idc/../templates/assets/asset_detail.html', locals())


def page_not_found(request):
    return render_to_response("404.html")

def index(request):
    print("index")
    return render_to_response("404.html")

#展示机房信息
def idcinfo(request):
    print("idc info'")
    idc_info = models.IDC.objects.all()
    for i in idc_info:
        print(i.name)
    print(idc_info)
    return render(request, 'idc/idc_info.html', locals())

#新增机房
def idcadd(request):
    print("add idcinfo")
    form=IdcForm()
    if request.method == "POST":
        form = IdcForm(request.POST)
        if form.is_valid():
            print("form valid.")
            #form_data = form.cleaned_data
            #print(form_data)
            #new_idc_obj = models.IDC(**form_data)
            #new_idc_obj.save()
            form.save()
            return HttpResponseRedirect('idcinfo/')
    else:
        form=IdcForm()
    print("通过ajax传参数过来，然后更新model")
    return render(request, 'idc/idc_add.html', locals())

#机房信息编辑
def idcinfo_edit(request):
    return
