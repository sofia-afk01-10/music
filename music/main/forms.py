from django import forms
from .models import Genre, Track
 
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
        fields = ['name', 'duretion', 'genre']
        labels = {
            'name': 'Название',
            'duretion': 'Длительность',
            'genre': 'Жанры',
        }