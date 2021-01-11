from django.contrib import admin

# Register your models here.

from .models import Genre, Movie, Comment

admin.site.register([Genre, Movie, Comment])
