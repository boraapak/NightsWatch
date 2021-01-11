from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from . import Movie


class Comment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    movie = models.ForeignKey(Movie, on_delete=models.RESTRICT)
    created_date = models.DateTimeField(default=datetime.utcnow)
    content = models.TextField()

    def __str__(self):
        return str(self.created_by) + ": " + self.content
