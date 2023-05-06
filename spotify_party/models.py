from django.db import models

#TODO: CHANGE MODELS TO FIT OUR NEEDS
class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    id_spotify = models.IntegerField(unique=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_expiration = models.DateField()

class Session(models.Model):
    id_session = models.IntegerField(primary_key=True)
    id_host = models.ForeignKey(User, on_delete=models.CASCADE)
    session_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class SessionMembers(models.Model):
    id_member = models.IntegerField(primary_key=True)
    id_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField()

class Playlist(models.Model):
    id_playlist = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

class MusicGenres(models.Model):
    id_genre = models.IntegerField(primary_key=True)
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    genre_name = models.CharField(max_length=50)

class Track(models.Model):
    id_track = models.IntegerField(primary_key=True)
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    duration = models.TimeField()

class Artist(models.Model):
    id_artist = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    popularity = models.CharField(max_length=50)

class ArtistTrack(models.Model):
    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id_track = models.ForeignKey(Track, on_delete=models.CASCADE)
