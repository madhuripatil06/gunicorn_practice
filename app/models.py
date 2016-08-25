from django.db import models

class Profile(models.Model):
    email = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')

