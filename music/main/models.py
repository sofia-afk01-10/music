from django.db import models

# Create your models here.
class Genre(models.Model):
    name_en = models.CharField(max_length=500)
    name_ru = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name_en
    
class Track(models.Model):
    name = models.CharField(max_length=500)
    duretion = models.FloatField()
    genre = models.ManyToManyField(Genre)
    def __str__(self):
        return self.name

class Genre_Track(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)