from django.contrib import admin
from django.urls import path
from spotify_party import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/join', views.AuthUserURL.as_view()),
    # path('api/auth/host', views.AuthHostURL.as_view()),
    #path('api/room', views.Room.as_view()),
    #path('api/room/<str:room_code>/', views.Room.as_view()),
    path('api/auth/join/callback', views.spotify_user_callback),
    # path('api/auth/host/callback', views.spotify_host_callback),
    path('api/auth/check', views.IsAuthenticated.as_view()),
    path('api/me/playlists', views.Playlists.as_view()),
    path('api/me/artists', views.TopArtists.as_view()),
    #path('api/me/genres', views.Genres.as_view()),
    path('api/me/albums', views.SavedAlbums.as_view()),
    #path('api/me/tracks', views.Tracks.as_view()),
    path('api/me/test', views.Test.as_view()), #FOR TESTING
]
