from django.db import models

class Story(models.Model):

    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    file = models.CharField(max_length=250)

    def __str__(self):
        return self.story_title + ' - ' + self.artist

