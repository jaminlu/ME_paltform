"""ManageEngine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from users.views import login_view, index, logout, register, profile, changepwd, profile_update
from .views import page_not_found
from django.conf.urls import handler404
import assets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('index', views.index,name="index"),
    url(r'^login/$', login_view, name='login'),
    path('index', index, name="index"),
    path('logout.html', logout, name="logout"),
    path('register.html', register, name="register"),
    path('profile.html', profile, name='profile'),
    path('profile_update.html', profile_update, name='profile_update'),
    path('changepwd.html', changepwd, name='changepwd'),

    # assets view
    path('assets/', include('assets.urls')),

]
handler404 = page_not_found
