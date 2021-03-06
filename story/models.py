"""
Models module containing the classes for the models
"""
from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone


class Story(models.Model):
    """
    Stores a single story entry, related to :model:`models.Story` and
    :model:`auth.User`.
    """
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


class Note(models.Model):
    """
    Stores a single note entry, related to :model:`models.Note` and
    :model:`auth.User`.
    """
    objects = None
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, )
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Stores a single comment entry, related to :model:`models.Comment`,
    :model:`auth.User` and :model:`models.Story`.
    """
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, )
    story = models.ForeignKey(Story, default=1, on_delete=models.CASCADE, )
    comment = models.TextField(max_length=500)
    date_commented = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.comment

