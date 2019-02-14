from django.db import models

# Create your models here.

class Assets(models.Model):
    hostname = models.CharField(max_length=32, blank=True, null=True)