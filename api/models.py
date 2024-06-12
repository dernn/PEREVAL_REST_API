from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=21)
