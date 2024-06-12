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
    coords = models.OneToOneField('Coords', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='new')
    level = models.ForeignKey('Level', on_delete=models.CASCADE)


class Coords(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    height = models.IntegerField()


class Level(models.Model):
    LEVEL_CHOICE = (
        ('н/к', 'н/к'),
        ('1A', '1A'),
        ('1B', '1B'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('3A', '3A'),
        ('3B', '3B'),
    )

    spring = models.CharField(max_length=2, choices=LEVEL_CHOICE, default='н/к')
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICE, default='н/к')
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICE, default='н/к')
    winter = models.CharField(max_length=2, choices=LEVEL_CHOICE, default='н/к')
