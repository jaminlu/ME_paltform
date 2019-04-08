from django.urls import path
from django.conf.urls import url
from idc import views


app_name = "idc"

urlpatterns = [
    path('', views.index, name='index',),
    path('index.html', views.index, name='index',),
    url(r'^idcinfo', views.idcinfo, name='idcinfo',),
    url(r'^idcadd', views.idcadd, name='idcadd',),
    url(r'^idcdetail/(\d+)', views.idcdetail, name='idcdetail',),
    url(r'^idcedit', views.idcinfo_edit, name='idcinfo_edit',),
]


