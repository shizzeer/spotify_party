from django.core.exceptions import ObjectDoesNotExist

from .models import SpotifyToken, FavouritePlaylist
from django.utils import timezone
from datetime import timedelta
from .credentials import CLIENT_ID, CLIENT_SECRET
from requests import post, put, get, RequestException

BASE_URL = "https://api.spotify.com/v1/"


def get_tokens(session_id):
    """
        Retrieves tokens from the database based on the Django user session ID.

        :param session_id: A string representing the session id.
        :return: A dictionary containing the tokens or None if the session does not exist.
    """

    tokens = SpotifyToken.objects.filter(user=session_id)

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
        # If tokens do not exist for the session ID, create a new SpotifyToken object
        tokens = SpotifyToken(user=session_id, access_token=access_token, refresh_token=refresh_token,
                              token_type=token_type, expires_in=expires_in)
        tokens.save()


def is_spotify_authenticated(session_id):
    tokens = get_tokens(session_id)
    if tokens:
        expiry = tokens.expires_in
        if expiry <= timezone.now():
            refresh_spotify_token(session_id)

        return True

    return False


def refresh_spotify_token(session_id):
    refresh_token = get_tokens(session_id).refresh_token

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')

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


def get_favorite_artists(session_id):
    """
    Retrieves the user's top artists.

    :param session_id: The user's session ID.
    :return: A list of dictionaries containing the user's favorite artists' names, IDs, images and popularity or an error dictionary.
    """
    artists = execute_spotify_api_request(session_id, "me/top/artists")
    if "Error" in artists:
        return artists
    return [
        {
            "name": artist["name"],
            "id": artist["id"],
            "image": artist["images"][0]["url"] if len(artist["images"]) > 0 else None,
            "popularity": artist["popularity"]
        } for artist in artists["items"]
    ]


def get_favorite_tracks(session_id):
    """
    Retrieves the user's favorite tracks.

    :param session_id: The user's session ID.
    :return: A list of dictionaries containing the user's favorite tracks' names, artists, IDs and preview URLs, or an error dictionary.
    """
    top_tracks_response = execute_spotify_api_request(session_id, "me/top/tracks")

    if 'Error' in top_tracks_response:
        return top_tracks_response

    favorite_tracks = []
    for track in top_tracks_response['items']:
        favorite_tracks.append({
            "name": track["name"],
            "id": track["id"],
        })

    return favorite_tracks

def get_favorite_genres(session_id):
    """
    Retrieves the user's favorite genres based on available genre seeds from the Spotify API.

    :param session_id: The user's session ID.
    :return: A list of the user's favorite genres or an error dictionary.
    """
    genre_seeds_response = execute_spotify_api_request(session_id, "recommendations/available-genre-seeds")

    if 'Error' in genre_seeds_response:
        return genre_seeds_response

    return genre_seeds_response['genres']


def get_favorite_albums(session_id):
    """
    Retrieves the user's favorite albums from their saved albums.

    :param session_id: The user's session ID.
    :return: A list of dictionaries containing the user's favorite albums' IDs, images, names and artists, or an error dictionary.
    """
    favorite_albums_response = execute_spotify_api_request(session_id, "me/albums")

    if 'Error' in favorite_albums_response:
        return favorite_albums_response

    favorite_albums = []
    for album in favorite_albums_response['items']:
        favorite_albums.append({
            "id": album["album"]["id"],
            "image": album["album"]["images"][0]["url"] if len(album["album"]["images"]) > 0 else None,
            "name": album["album"]["name"],
            "artist": album["album"]["artists"][0]["name"]
        })

    return favorite_albums


def retrieve_tracks_from_playlists_in_db(session_id):
    """
    Retrieves the user's tracks from favorite playlists in the database.

    :param session_id: The user's session ID.
    :return: A list of dictionaries containing the user's tracks (ID) or an error dictionary.
    """
    # Get the user's Spotify token
    spotify_token = get_tokens(session_id)

    # Get the user's favorite playlists
    favorite_playlists = FavouritePlaylist.objects.filter(spotify_token=spotify_token)

    # Get the track IDs from each playlist
    track_ids = []
    for playlist in favorite_playlists:
        playlist_id = playlist.playlist.id
        playlist_tracks_endpoint = f"playlists/{playlist_id}/tracks?fields=items(track(id))"
        response = execute_spotify_api_request(session_id, playlist_tracks_endpoint)

        if 'Error' in response:
            return {'Error': response['Error']}

        # Parse the track IDs from the API response
        track_ids.extend([item['track']['id'] for item in response['items']])

    # Return the list of track IDs
    return track_ids




