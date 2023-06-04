CLIENT_ID = "9486820ad2a24e1f8a847fbb55ff9da8"
CLIENT_SECRET = "2a85936eaf744fbba11653b44de767fd"
REDIRECT_CALLBACK_JOIN_URI = "http://127.0.0.1:8000/api/auth/join/callback"
REDIRECT_CALLBACK_HOST_URI = "http://127.0.0.1:8000/api/auth/host/callback"

'''
Available scopes, more at: https://developer.spotify.com/documentation/web-api/concepts/scopes
'''

USER_SCOPES = [
    'playlist-read-private',        # Read access to user's private playlists
    'playlist-read-collaborative',  # Read access to user's collaborative playlists
    'user-follow-read',             # Read access to the list of artists followed by the user
    'user-top-read',                # Read access to user's top artists and tracks
    'user-read-recently-played',    # Read access to user's recently played tracks
    'user-library-read',            # Read access to user's saved tracks and albums
    'user-read-email',              # Read access to user's email address
    'user-read-private',            # Read access to user's private account information
    'user-read-currently-playing',  # Read access to user's currently playing track
    'user-read-playback-state',     # Read access to user's current playback state
    'user-read-playback-position'   # Read access to user's playback position in the current episode of a podcast
]

HOST_SCOPES = [
    'ugc-image-upload',               # Upload user-generated playlist cover images
    'playlist-modify-public',         # Modify and read public playlists
    'playlist-modify-private',        # Modify and read private playlists
    'playlist-read-private',          # Read access to user's private playlists
    'playlist-read-collaborative',    # Read access to user's collaborative playlists
    'user-library-modify',            # Modify and read user's saved tracks and albums
    'user-library-read',               # Read access to user's saved tracks and albums
    'user-follow-modify',             # Modify and read user's followed artists
    'user-follow-read',               # Read access to the list of artists followed by the user
    'user-read-private',              # Read user's private account information
    'user-read-email',                # Read user's email address
    'user-read-playback-state',       # Read user's current playback state
    'user-read-currently-playing',    # Read user's currently playing track
    'user-modify-playback-state',     # Control user's playback state
    'user-read-recently-played',      # Read user's recently played tracks
    'user-top-read',                  # Read access to user's top artists and tracks
    'user-read-playback-position',    # Read user's playback position in the current episode of a podcast
]