from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    photo_url = models.URLField()
    trailer_url = models.URLField()
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    duration = models.DurationField()
    directors = models.TextField()
    cast = models.TextField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
