from django.urls import path, include
from . import views

urlpatterns = [
    path('alert/', views.alert , name='alert'),
]