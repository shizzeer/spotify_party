from django.shortcuts import redirect
from .credentials import CLIENT_SECRET, CLIENT_ID, USER_SCOPES, REDIRECT_CALLBACK_JOIN_URI
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response

from .util import *


class AuthUserURL(APIView):
    """ Handles the authorization process for users with Spotify API. """

    def get(self, request):
        """
        Handles GET requests and returns a URL for user authorization.

        :param request: An HttpRequest object representing the request.
        :return: A JsonResponse containing the authorization URL and an HTTP 200 status code.
        """

        # Join user scopes (permissions) into a single space-separated string
        scopes = ' '.join(USER_SCOPES)

        # Construct the authorization URL
        url = Request(
            method='GET',
            url='https://accounts.spotify.com/authorize',
            params={
                'scope': scopes,
                'response_type': 'code',
                'redirect_uri': REDIRECT_CALLBACK_JOIN_URI,
                'client_id': CLIENT_ID,
            }
        ).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


def spotify_user_callback(request):
    """
    Handles the callback from the Spotify API after user authorization.
    It retrieves the authorization code, exchanges it for an access token, and stores the
    tokens in the database for the current session.

    :param request: An HttpRequest object representing the request.
    :return: A redirect to the specified URL.
    """

    REDIRECT_URL = 'http://localhost:3000/join'

    # Get the authorization code from the request's GET parameters
    code = request.GET.get('code')

    # Send a POST request to exchange the authorization code for an access token
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_CALLBACK_JOIN_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    set_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    # TODO: CHANGE URL (FOR TESTING PURPOSES ONLY)
    return redirect('http://127.0.0.1:8000/api/auth/check')


class IsAuthenticated(APIView):
    def get(self, request):
        print(f"Session ID: {self.request.session.session_key}")
        is_authenticated = is_spotify_authenticated(self.request.session.session_key)
        print(is_authenticated)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)


class Playlists(APIView):
    """
    A class-based view to retrieve the playlist of the current user.
    """

    def get(self, request):
        session_id = self.request.session.session_key

        # Get the playlist of the current user
        playlists = get_playlists(session_id)

        # Return the retrieved playlist with a 200 OK status
        return Response(playlists, status=status.HTTP_200_OK)

    def post(self, request):
        session_id = self.request.session.session_key

        # Get the selected playlists from the request data
        selected_playlists = request.data.get("selected_playlists")

        # Retrieve user session from database
        user = get_tokens(session_id)

        save_playlists_to_db(user, selected_playlists)

        # Return a success response with a 200 OK status
        return Response(
            {"message": "Selected playlists have been added to favourites."},
            status=status.HTTP_200_OK,
        )


class TopArtists(APIView):
    """
    A class-based view to retrieve the top artists of the current user.
    """

    def get(self, request):
        session_id = self.request.session.session_key

        # Get the top artists of the current user
        top_artists = get_top_artists(session_id)

        # Return the retrieved top artists with a 200 OK status
        return Response(top_artists, status=status.HTTP_200_OK)

    def post(self, request):
        session_id = self.request.session.session_key

        # Get the selected artists from the request data
        selected_artists = request.data.get("selected_artists")

        # Retrieve user session from database
        user = get_tokens(session_id)

        save_artists_to_db(user, selected_artists)

        # Return a success response with a 200 OK status
        return Response(
            {"message": "Selected artists have been added to favourites."},
            status=status.HTTP_200_OK,
        )


class SavedAlbums(APIView):
    """
    A class-based view to retrieve saved albums of the current user.
    """

    def get(self, request):
        session_id = self.request.session.session_key

        # Get saved albums of the current user
        saved_albums = get_saved_albums(session_id)

        # Return the retrieved saved albums with a 200 OK status
        return Response(saved_albums, status=status.HTTP_200_OK)

    def post(self, request):
        session_id = self.request.session.session_key

        # Get the selected albums from the request data
        selected_albums = request.data.get("selected_albums")

        # Retrieve user session from database
        user = get_tokens(session_id)

        save_albums_to_db(user, selected_albums)

        # Return a success response with a 200 OK status
        return Response(
            {"message": "Selected albums have been added to favourites."},
            status=status.HTTP_200_OK,
        )


class Test(APIView):
    def get(self, request):
        session_id = self.request.session.session_key

        # Get all tracks associated with the current user
        user_tracks = get_user_track_ids(session_id)

        # Return the retrieved tracks with a 200 OK status
        return Response(user_tracks, status=status.HTTP_200_OK)

#
# class Genres(APIView):
#     """
#     A class-based view to retrieve the genres available in the Spotify catalog.
#     """
#
#     def get(self, request):
#         session_id = self.request.session.session_key
#         genres = get_favorite_genres(session_id)
#         return Response(genres, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         # Get the session ID for the current user
#         session_id = self.request.session.session_key
#
#         # Get the Spotify token associated with the session ID
#         spotify_token = SpotifyToken.objects.get(user=session_id)
#
#         # Parse the list of favorite genres from the request data
#         favorite_genres = request.data.get('favorite_genres', [])
#
#         # Add each favorite genre to the database
#         for genre_name in favorite_genres:
#             # Get or create the genre object based on the name
#             genre, _ = Genre.objects.get_or_create(name=genre_name)
#
#             # Create a FavoriteGenre object to associate the genre with the Spotify token
#             favorite_genre = FavouriteGenre.objects.create(
#                 spotify_token=spotify_token,
#                 genre=genre
#             )
#
#         # Return a success response
#         return Response({'message': 'Favorite genres added successfully.'}, status=status.HTTP_200_OK)
#
#
# class Albums(APIView):
#     """
#     A class-based view to retrieve the favorite albums of the current user.
#     """
#
#     def get(self, request):
#         session_id = self.request.session.session_key
#         favorite_albums = get_favorite_albums(session_id)
#         return Response(favorite_albums, status=status.HTTP_200_OK)
#
#
# class Compute(APIView):
#     def get(self, request):
#         session_id = self.request.session.session_key
#         test = retrieve_tracks_from_playlists_in_db(session_id)
#         return Response(test, status=status.HTTP_200_OK)
#
#
# class Tracks(APIView):
#     """
#     A class-based view to retrieve the favorite tracks of the current user.
#     """
#
#     def get(self, request):
#         session_id = self.request.session.session_key
#         favorite_tracks = get_favorite_tracks(session_id)
#         return Response(favorite_tracks, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         # Get the session ID for the current user
#         session_id = self.request.session.session_key
#
#         # Get the Spotify token associated with the session ID
#         spotify_token = SpotifyToken.objects.get(user=session_id)
#
#         # Parse the list of favorite tracks from the request data
#         favorite_tracks = request.data.get('favorite_tracks', [])
#
#         # Add each favorite track to the database
#         for track_id in favorite_tracks:
#             # Get or create the track object based on the ID
#             track, _ = Track.objects.get_or_create(id=track_id)
#
#             # Create a FavouriteTrack object to associate the track with the Spotify token
#             favorite_track = FavouriteTrack.objects.create(
#                 spotify_token=spotify_token,
#                 track=track
#             )
#
#         # Return a success response
#         return Response({'message': 'Favorite tracks added successfully.'}, status=status.HTTP_200_OK)
