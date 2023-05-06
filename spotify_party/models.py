from django.db import models

#TODO: CHANGE MODELS TO FIT OUR NEEDS

class SpotifyToken(models.Model):
    user = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)


class Artist(models.Model):
    id = models.CharField(max_length=255, primary_key=True)


class Playlist(models.Model):
    id = models.CharField(max_length=255, primary_key=True)


class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)


class Track(models.Model):
    id = models.CharField(max_length=255, primary_key=True)


class FavouritePlaylist(models.Model):
    spotify_token = models.ForeignKey(SpotifyToken, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)


class FavouriteArtist(models.Model):
    spotify_token = models.ForeignKey(SpotifyToken, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class FavouriteGenre(models.Model):
    spotify_token = models.ForeignKey(SpotifyToken, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class FavouriteTrack(models.Model):
    spotify_token = models.ForeignKey(SpotifyToken, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
