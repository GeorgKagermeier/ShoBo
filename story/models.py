from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone


class Story(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)


class Note(models.Model):
    objects = None
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, )
    title = models.CharField(default="", max_length=500)
    text = models.TextField(default="", max_length=1000)
    date_added = models.DateTimeField(default=django.utils.timezone.now)



