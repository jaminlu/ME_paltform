from django.urls import path
from django.conf.urls import url
from .views import assetinfo

app_name = 'assets'

urlpatterns = [
    url(r'^assetinfo', view=assetinfo, name='assetinfo'),
]
