from django import forms
from .models import Genre, Track, Artist
 
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_en', 'name_ru', 'description']
        labels = {
            'name_en': 'Название на английском',
            'name_ru': 'Название на русским',
            'description': 'Описание',
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name', 'duretion', 'genre', 'artist']
        labels = {
            'name': 'Название',
            'duretion': 'Длительность',
            'genre': 'Жанры',
            'artist': 'Артист',
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Имя / название',
            'image': 'Фотография',
        }