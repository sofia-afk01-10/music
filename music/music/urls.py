
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('main', views.main),
    path('genres', views.genre_music), 
    path('tracks', views.track_music), 
    path('deleteop/<int:id_genre>',views.deleteop),
    path('edit_genre/<int:id_genre>', views.edit_genre),
    path('edit_track/<int:id_track>', views.edit_track),
    path('deleteop_track/<int:id_track>',views.deleteop_track),
    path('add_track/', views.add_track),
    path('add_genre/', views.add_genre),
    path('artists/', views.artists),
    path('add_artist/', views.add_artist),
    path('media/<int:id_artist>', views.artists),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
