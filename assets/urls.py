from django.urls import path
from django.conf.urls import url
from assets import views


app_name = "asset"

urlpatterns = [
    path('', views.assetinfo, name='assetsinfo'),
    path('index.html', views.index, name='index'),
    url(r'^assetinfo',views.assetinfo,name='assetinfo'),
    url(r'^idcinfo', views.idcinfo, name='idcinfo'),
    url(r'^idcadd', views.idcadd, name='idcadd'),
]


