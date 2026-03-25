from django.contrib import admin
from .models import Genre, Genre_Track, Track

# Register your models here.
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Genre_Track)