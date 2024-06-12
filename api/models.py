from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=21)


class Pereval(models.Model):
    STATUS_CHOICE = (
        ('new', 'new'),
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    )

    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # coords = None
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='new')
    # level = None
