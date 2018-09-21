from django.urls import path
from . import views

urlpatterns = [
   path('users/login/', views.login, name='login'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('user_list/', views.user_list, name='user_list'),
   path('user_add/', views.user_add, name='user_add'),
]