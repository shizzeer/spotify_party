import random
import string
from django.shortcuts import redirect

from .models import Room, RoomParticipant
from .credentials import CLIENT_SECRET, CLIENT_ID, USER_SCOPES, HOST_SCOPES, REDIRECT_CALLBACK_JOIN_URI, REDIRECT_CALLBACK_HOST_URI
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action 

from .util import * 
from .playlists_merging import *


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


class AuthHostURL(APIView):
    """ Handles the authorization process for users-hosts with Spotify API. """

    def get(self, request):
        """
        Handles GET requests and returns a URL for user authorization.

        :param request: An HttpRequest object representing the request.
        :return: A JsonResponse containing the authorization URL and an HTTP 200 status code.
        """

        # Join hosts scopes (permissions) into a single space-separated string
        scopes = ' '.join(HOST_SCOPES)

        # Construct the authorization URL
        url = Request(
            method='GET',
            url='https://accounts.spotify.com/authorize',
            params={
                'scope': scopes,
                'response_type': 'code',
                'redirect_uri': REDIRECT_CALLBACK_HOST_URI,
                'client_id': CLIENT_ID,
            }
        ).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


def spotify_host_callback(request):
    """
    Handles the callback from the Spotify API after user-host authorization.
    It retrieves the authorization code, exchanges it for an access token, and stores the
    tokens in the database for the current session.

    :param request: An HttpRequest object representing the request.
    :return: A redirect to the specified URL.
    """

    REDIRECT_URL = 'http://127.0.0.1:3000/host'

    # Get the authorization code from the request's GET parameters
    code = request.GET.get('code')

    # Send a POST request to exchange the authorization code for an access token
    spotify_response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_CALLBACK_HOST_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = spotify_response.get('access_token')
    token_type = spotify_response.get('token_type')
    refresh_token = spotify_response.get('refresh_token')
    expires_in = spotify_response.get('expires_in')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    set_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    #TODO: NOT SAFE FOR PRODUCTION
    response = redirect(REDIRECT_URL)
    response.set_cookie('sessionid', request.session.session_key, path='/host')
    return response


def spotify_user_callback(request):
    """
    Handles the callback from the Spotify API after user authorization.
    It retrieves the authorization code, exchanges it for an access token, and stores the
    tokens in the database for the current session.

    :param request: An HttpRequest object representing the request.
    :return: A redirect to the specified URL.
    """

    REDIRECT_URL = 'http://127.0.0.1:3000/join'

    # Get the authorization code from the request's GET parameters
    code = request.GET.get('code')

    # Send a POST request to exchange the authorization code for an access token
    spotify_response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_CALLBACK_JOIN_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = spotify_response.get('access_token')
    token_type = spotify_response.get('token_type')
    refresh_token = spotify_response.get('refresh_token')
    expires_in = spotify_response.get('expires_in')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    set_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    #TODO: NOT SAFE FOR PRODUCTION
    response = redirect(REDIRECT_URL)
    response.set_cookie('sessionid', request.session.session_key, path='/join')
    return response


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
    
class RoomView(APIView):
    """
    A class-based view to create and join rooms based on session code.
    """

    def create(self, request):
        user_id = self.request.session.session_key
        user = User.objects.get(id_user=user_id)
        # Generate unique code for a room
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        room = Room.objects.create(host=user, code=code)
        room.save()

        # Add host user as a first room participant
        roomParticipant = RoomParticipant.objects.create(user=user, room=room)
        roomParticipant.save()

        return Response({'room_code': code})

    def join(self, request):
        room_code = request.data.get('room_code')
        user_id = self.request.session.session_key
        user = User.objects.get(id_user=user_id)
        try:
            room = Room.objects.get(code=room_code)
            try:
                room_participant = RoomParticipant.objects.get(room_id=room_code, user_id=user_id)
                return Response({'error': 'User already joined this room'})
            except RoomParticipant.DoesNotExist:
                RoomParticipant.objects.create(user=user, room=room)
                return Response({'room_code': room_code})
        except Room.DoesNotExist:
            return Response({'error': 'Room not found'}, status=404)

    def post(self, request):
        action = request.data.get('action')
        if action == 'create':
            return self.create(request)
        elif action == 'join':
            return self.join(request)
        else:
            return Response({'error': 'Invalid action'}, status=400)


class SearchTracks(APIView):
    """
    A class-based view to search tracks in Spotify.
    """

    def get(self, request):
        session_id = self.request.session.session_key
        query = request.GET.get('q')

        if query is None:
            return Response({'Error': 'Missing query parameter'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the tracks from Spotify
        tracks = get_tracks(session_id, query)

        # Return the retrieved tracks with a 200 OK status
        return Response(tracks, status=status.HTTP_200_OK)
    
class MergePlaylists(APIView):
    """
    A class-based view to merge playlists of users from a common room.
    """

    def post(self, request):
        session_id = self.request.session.session_key

        # Get the selected albums from the request data
        room_code = request.data.get("room_code")

        common_tracks = get_common_tracks_for_room(room_code)

        user = get_tokens(session_id)
        playlist_name = create_playlist_for_room(room_code, user, common_tracks)
        print(playlist_name)

        return Response("Your playlist is created! Name: " + playlist_name ,status=status.HTTP_200_OK)





