from django.contrib.auth.models import Permission, User
from django.db import models

class Story(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    file = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist




