from django.db import models

# Create your models here.

class Alter(models.Model):
    text = models.TextField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    gen_time = models.DateTimeField(auto_now_add=True)