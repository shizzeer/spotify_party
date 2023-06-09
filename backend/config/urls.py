from django.contrib import admin
from django.urls import path
from spotify_party import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/join', views.AuthUserURL.as_view()),
    path('api/auth/host', views.AuthHostURL.as_view()),
    path('api/auth/join/callback', views.spotify_user_callback),
    path('api/auth/host/callback', views.spotify_host_callback),
    path('api/auth/check', views.IsAuthenticated.as_view()),
    path('api/me/playlists', views.Playlists.as_view()),
    path('api/me/artists', views.TopArtists.as_view()),
    path('api/me/albums', views.SavedAlbums.as_view()),
    path('api/me/must-have', views.SearchTracks.as_view()),
    #path('api/me/tracks', views.Tracks.as_view()),
    path('api/room', views.RoomView.as_view()),
    path('api/merge_playlists', views.MergePlaylists.as_view()),
]
