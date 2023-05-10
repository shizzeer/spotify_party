from django.db import models


class User(models.Model):
    id_user = models.CharField(primary_key=True, max_length=255)
    id_spotify = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=255)
    expires_in = models.DateTimeField()
    refresh_token = models.CharField(max_length=255)


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
    id_playlist = models.CharField(primary_key=True, max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class Track(models.Model):
    id_track = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    duration = models.IntegerField()


class PlaylistTrack(models.Model):
    id_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)


class MusicGenre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_name = models.CharField(max_length=50)


class MusicGenreTrack(models.Model):
    id_genre = models.ForeignKey(MusicGenre, on_delete=models.CASCADE)
    id_track = models.ForeignKey(Track, on_delete=models.CASCADE)


class Artist(models.Model):
    id_artist = models.CharField(primary_key=True, max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    popularity = models.CharField(max_length=50)


class ArtistTrack(models.Model):
    id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id_track = models.ForeignKey(Track, on_delete=models.CASCADE)


class Album(models.Model):
    id_album = models.CharField(primary_key=True, max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class AlbumTrack(models.Model):
    id_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    id_track = models.ForeignKey(Track, on_delete=models.CASCADE)
