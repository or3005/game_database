from django.db import models
from PIL import Image


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        img = img.resize((600, 600), Image.Resampling.LANCZOS)
        img.save(self.poster.path)

    def __str__(self):
        return self.title
