from django.db import models

import datetime
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField('email', max_length=20, blank=True)
    dep = models.CharField('department', max_length=46, blank=True)
    tel = models.CharField('telephone', max_length=20, blank=True)
    sex = models.CharField('sex', max_length=4, blank=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()



