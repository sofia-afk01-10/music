from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm


# Create your views here.
def main(request):
    return render(request, 'index.html', {'page': 'main'})

def genre_music(request):
    genres = Genre.objects.all() 
    return render(request, 'genres.html', {'genres': genres, 'page': 'genres'})

def track_music(request):
    tracks = Track.objects.all() 
    artists = Artist.objects.all()
    artist = None
    if request.method == "POST":
        id_artist = request.POST.get('artist')
        artist = Artist.objects.get(id=id_artist)
        tracks = Track.objects.filter(artist=artist)
    return render(request, 'track.html', {'tracks': tracks, 'artists':artists, 'current_artist': artist, 'page': 'tracks'})

def edit_genre(request, id_genre):
    g = Genre.objects.get(id=id_genre)
    print(g)
    
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm(instance=g)
        return render(request, "update_genre.html", {'form': genreform})


def deleteop(request,id_genre):
    genre = Genre.objects.get(id=id_genre)
    genre.delete()
    return HttpResponse('<h1>Описание успешно удалено</h1><br><a href="/">На главную</a>')

def add_genre(request):
    if request.method == "POST":
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        desc = request.POST.get("description")
        genre=Genre()
        genre.name_en = name_en
        genre.name_ru = name_ru
        genre.description =desc
        genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form':genreform})
    
def edit_track(request, id_track):
    t = Track.objects.get(id=id_track)
    print(t)
    
    if request.method == "POST":
        track = TrackForm(request.POST, instance=t)
        if track.is_valid():
            track.save()
        return redirect('/tracks')
    else:
        trackform = TrackForm(instance=t)
        return render(request, "update_track.html", {'form': trackform})
    
def deleteop_track(request,id_track):
    track = Track.objects.get(id=id_track)
    track.delete()
    return HttpResponse('<h1>Трек успешно удален</h1><br><a href="/">На главную</a>')

def add_track(request):
    if request.method == "POST":
        track = TrackForm(request.POST)
        if track.is_valid():
            track.save()
        return redirect('/tracks')
    else:
        trackform = TrackForm()
        return render(request, "add_track.html", {'form': trackform})

    
# исполнители
def artists(request):
    # получим список имполнителей из базы
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})

def add_artist(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.POST.get("image")
        artist=Artist()
        artist.name = name
        artist.image = image
        artist.save()
        return redirect('/genres')
    else:
        artistform = ArtistForm()
        return render(request, "add_artist.html", {'form':artistform})

