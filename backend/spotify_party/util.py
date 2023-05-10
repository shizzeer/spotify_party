from django.utils import timezone
from datetime import timedelta
from .credentials import CLIENT_ID, CLIENT_SECRET
from requests import post, put, get, RequestException
from .models import User, Playlist, Track, MusicGenre, PlaylistTrack, Artist, ArtistTrack, AlbumTrack, Album

BASE_URL = "https://api.spotify.com/v1/"


def get_tokens(session_id):
    """
        Retrieves tokens from the database based on the Django user session ID.

        :param session_id: A string representing the session id.
        :return: A dictionary containing the tokens or None if the session does not exist.
    """

    tokens = User.objects.filter(id_user=session_id)

    if tokens.exists():
        return tokens[0]
    else:
        return None


def set_tokens(session_id, access_token, token_type, expires_in, refresh_token):
    """
        Stores or updates tokens in the database for the given session ID.

        :param session_id: A string representing the session key.
        :param access_token: A string representing the access token.
        :param token_type: A string representing the token type.
        :param expires_in: An integer representing the token's expiration time in seconds.
        :param refresh_token: A string representing the refresh token.
    """

    # Get the existing tokens for the session ID
    tokens = get_tokens(session_id)
    # Calculate the expiration time
    expires_in = timezone.now() + timedelta(seconds=expires_in)

    if tokens:
        # If tokens exist for the session ID, update them
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.save(update_fields=['access_token', 'refresh_token', 'expires_in', 'token_type'])
    else:
        # If tokens do not exist for the session ID, create a new User object
        user_details = get_user_info(access_token)

        tokens = User(id_user=session_id, id_spotify=user_details['id'], username=user_details['display_name'],
                      access_token=access_token, email=user_details['email'], refresh_token=refresh_token,
                      token_type=token_type, expires_in=expires_in)
        tokens.save()


def get_user_info(access_token):
    """
    Fetches the user's information from the Spotify API using the provided access token.

    :param access_token: A string representing the access token.
    :return: A dictionary containing user information, or None if the request was unsuccessful.
    """

    # Set the authorization header with the provided access token
    headers = {"Authorization": f"Bearer {access_token}"}

    # Send a GET request to the Spotify API's 'me' endpoint to fetch user information
    response = get(BASE_URL + 'me', headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # If successful, return the user information as a dictionary
        return response.json()
    else:
        # If the request was unsuccessful, log the error and return None
        print(f"Error fetching user info: {response.status_code} - {response.text}")
        return None


def is_spotify_authenticated(session_id):
    """
    Checks if the current session has an authenticated Spotify user.

    :param session_id: A string representing the session key.
    :return: A boolean value representing the authentication status.
    """

    # Get the tokens associated with the given session ID
    tokens = get_tokens(session_id)

    # Check if the tokens exist for the session ID
    if tokens:
        # Get the expiration datetime of the access token
        expiry = tokens.expires_in

        # Check if the access token is expired
        if expiry <= timezone.now():
            # If the access token is expired, refresh it
            refresh_spotify_token(session_id)

        # If tokens exist and are not expired, the user is authenticated
        return True

    # If tokens do not exist for the session ID, the user is not authenticated
    return False


def refresh_spotify_token(session_id):
    """
    Refreshes the Spotify access token for the given session ID.

    :param session_id: A string representing the session key.
    """

    # Get the refresh token associated with the session ID
    refresh_token = get_tokens(session_id).refresh_token

    # Send a POST request to the Spotify API token endpoint with the necessary data for token refresh
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    # Extract the new access token, token type, and expiration time from the response
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')

    # Update the tokens in the database using the set_tokens function
    set_tokens(session_id, access_token, token_type, expires_in, refresh_token)


def execute_spotify_api_request(session_id, endpoint, method="GET", data=None):
    """
    Executes a Spotify API request.

    :param session_id: The user's session ID.
    :param endpoint: The API endpoint to request.
    :param method: The HTTP method to use for the request (default is 'GET').
    :param data: Optional data to include in the request.
    :return: JSON response from the API request or an error dictionary.
    """
    tokens = get_tokens(session_id)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {tokens.access_token}",
    }

    try:
        if method == "GET":
            response = get(BASE_URL + endpoint, headers=headers)
        elif method == "POST":
            response = post(BASE_URL + endpoint, headers=headers, json=data)
        elif method == "PUT":
            response = put(BASE_URL + endpoint, headers=headers, json=data)
        else:
            return {'Error': 'Invalid HTTP method'}

        response.raise_for_status()
        return response.json()
    except RequestException as e:
        return {'Error': f"Issue with request: {str(e)}"}


def get_playlists(session_id):
    """
    Retrieves the user's playlists.

    :param session_id: The user's session ID.
    :return: A list of dictionaries containing the user's playlists' names, images and IDs, or an error dictionary.
    """
    playlists = execute_spotify_api_request(session_id, "me/playlists")
    if "Error" in playlists:
        return playlists

    return [
        {
            "name": playlist["name"],
            "image": playlist["images"][0]["url"] if len(playlist["images"]) > 0 else None,
            "id": playlist["id"],
            "description": playlist["description"]
        } for playlist in playlists["items"]
    ]


def get_top_artists(session_id, limit=20, time_range='medium_term'):
    """
    Retrieves the user's top artists.

    :param session_id: The user's session ID.
    :param limit: The maximum number of artists to retrieve.
    :param time_range: The time range for which to retrieve the top artists.
    :return: A list of dictionaries containing the user's top artists' names, images, IDs, and genres, or an error dictionary.
    """
    top_artists = execute_spotify_api_request(session_id, f"me/top/artists?limit={limit}&time_range={time_range}")
    if "Error" in top_artists:
        return top_artists

    return [
        {
            "name": artist["name"],
            "image": artist["images"][0]["url"] if len(artist["images"]) > 0 else None,
            "id": artist["id"],
            "genres": artist["genres"],
            "popularity": artist["popularity"]
        } for artist in top_artists["items"]
    ]


def get_saved_albums(session_id):
    """
    Retrieves the user's saved albums

    :param session_id: The user's session ID.
    :return: A list of dictionaries containing the user's saved albums' names, images, IDs, and genres, or an error dictionary.
    """
    saved_albums = execute_spotify_api_request(session_id, "me/albums")
    if "Error" in saved_albums:
        return saved_albums

    albums = []
    for album in saved_albums["items"]:
        album_info = album["album"]
        album_dict = {
            "name": album_info["name"],
            "image": album_info["images"][0]["url"] if album_info["images"] else None,
            "id": album_info["id"]
        }

        albums.append(album_dict)
    return albums


def save_playlists_to_db(user, selected_playlists):
    try:
        for playlist in selected_playlists:
            new_playlist = Playlist(
                id_playlist=playlist['id'],
                id_user=user,
                name=playlist['name'],
                description=playlist['description']
            )
            new_playlist.save()

            playlist_tracks = retrieve_tracks_from_playlist(user.id_user, playlist['id'])
            for track in playlist_tracks:
                new_track = Track(
                    id_track=track['id'],
                    name=track['name'],
                    album=track['album'],
                    duration=track['duration_ms']
                )
                new_track.save()

                new_playlist_track = PlaylistTrack(
                    id_playlist=new_playlist,
                    id_track=new_track
                )
                new_playlist_track.save()

    except User.DoesNotExist:
        print(f"User with id {user['user_id']} does not exist")


def retrieve_tracks_from_playlist(session_id, playlist_id):
    """
    Retrieves the tracks from a playlist.

    :param session_id: The user's session ID.
    :param playlist_id: The playlist's ID.
    :return: A list of dictionaries containing the playlist's tracks or an error dictionary.
    """

    # Execute the API request to retrieve the playlist
    playlist = execute_spotify_api_request(session_id, f"playlists/{playlist_id}")
    if "Error" in playlist:
        return playlist

    # Extract the track information from the playlist
    tracks = []
    for item in playlist["tracks"]["items"]:
        track_info = item["track"]
        track = {
            "name": track_info["name"],
            "id": track_info["id"],
            "album": track_info["album"]["name"],
            "duration_ms": track_info["duration_ms"]
        }
        tracks.append(track)
    return tracks


def retrieve_tracks_from_album(session_id, album_id):
    """
    Retrieves the tracks from an album.

    :param session_id: The user's session ID.
    :param album_id: The album's ID.
    :return: A list of dictionaries containing the album's tracks or an error dictionary.
    """

    # Execute the API request to retrieve the album
    album = execute_spotify_api_request(session_id, f"albums/{album_id}")
    if "Error" in album:
        return album

    # Extract the track information from the album
    tracks = []
    for track_info in album["tracks"]["items"]:
        track = {
            "name": track_info["name"],
            "id": track_info["id"],
            "album": album["name"],
            "duration_ms": track_info["duration_ms"]
        }
        tracks.append(track)
    return tracks


def save_artists_to_db(user, selected_artists):
    try:
        for artist in selected_artists:
            new_artist = Artist(
                id_artist=artist['id'],
                id_user=user,
                name=artist['name'],
                popularity=artist['popularity']
            )
            new_artist.save()

            save_top_artist_tracks_to_db(user.id_user, new_artist)

            genres = artist['genres']
            # Saving genres of the artist
            for genre in genres:
                new_genre = MusicGenre(
                    genre_name=genre,
                    id_user=user,
                )
                new_genre.save()

    except User.DoesNotExist:
        print(f"User with id {user['user_id']} does not exist")


def save_top_artist_tracks_to_db(session_id, artist):
    try:
        # Get the top tracks of the artist
        top_tracks = execute_spotify_api_request(session_id, f"artists/{artist.id_artist}/top-tracks?market=US")["tracks"]

        # Save each top track to the database
        for track in top_tracks:
            new_track = Track(
                id_track=track["id"],
                name=track["name"],
                album=track["album"]["name"],
                duration=track["duration_ms"]
            )
            new_track.save()

            # Link the track to the artist
            new_artist_track = ArtistTrack(
                id_artist=artist,
                id_track=new_track
            )
            new_artist_track.save()

    except Exception as e:
        print(f"Error saving top tracks for artist with id {artist.id_artist}: {e}")


def save_albums_to_db(user, selected_albums):
    try:
        for album in selected_albums:
            new_album = Album(
                id_album=album['id'],
                id_user=user,
                name=album['name'],
            )
            new_album.save()

            album_tracks = retrieve_tracks_from_album(user.id_user, album['id'])
            for track in album_tracks:
                new_track = Track(
                    id_track=track['id'],
                    name=track['name'],
                    album=track['album'],
                    duration=track['duration_ms']
                )
                new_track.save()

                new_album_track = AlbumTrack(
                    id_album=new_album,
                    id_track=new_track
                )
                new_album_track.save()

    except User.DoesNotExist:
        print(f"User with id {user['user_id']} does not exist")


def get_user_track_ids(user_id):
    # Get all tracks associated with user's playlists
    playlist_tracks = PlaylistTrack.objects.filter(id_playlist__id_user=user_id).values_list("id_track__id_track", flat=True)
    # Get all tracks associated with user's albums
    album_tracks = AlbumTrack.objects.filter(id_album__id_user=user_id).values_list("id_track__id_track", flat=True)
    # Get all tracks associated with user's artists
    artist_tracks = ArtistTrack.objects.filter(id_artist__id_user=user_id).values_list("id_track__id_track", flat=True)
    # Concatenate all track querysets and remove duplicates
    track_ids = set(list(playlist_tracks) + list(album_tracks) + list(artist_tracks))
    return list(track_ids)
# def get_favorite_genres(session_id):
#     """
#     Retrieves the user's favorite genres based on available genre seeds from the Spotify API.
#
#     :param session_id: The user's session ID.
#     :return: A list of the user's favorite genres or an error dictionary.
#     """
#     genre_seeds_response = execute_spotify_api_request(session_id, "recommendations/available-genre-seeds")
#
#     if 'Error' in genre_seeds_response:
#         return genre_seeds_response
#
#     return genre_seeds_response['genres']
#

