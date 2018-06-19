from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone

class Story(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    file = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.artist


class Note(models.Model):
    note = models.TextField()
    date_added = models.DateTimeField(default=django.utils.timezone.now)


