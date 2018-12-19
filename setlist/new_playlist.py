from get_data import *

# Design flow

# Get the playlist information
# Remove all the songs from the playlist
# Assign grouping and ordering within that group
# Shuffle those groups from a high level
# Put shuffled music back into the playlist with the new ordering


SPOTIPY_CLIENT_ID = # your ID here
SPOTIPY_CLIENT_SECRET = # your secret here
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

scope = 'playlist-modify-public'
username = "frog_bird"
playlist_name = "My Test Playlist"
scope = 'playlist-read-private'

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

playlistid, spot = get_playlist_id(username, playlist_name)

# get tracks from the playlist first

tracklist = get_playlist_tracks(username, playlistid, spot)

# remove playlist tracks





# make recursive mark down thing for ethan

# JSON

# keep dictionary of ID -> group number
# keep dictionary of group number -> [id, id, id, id]
# keep ordering easily, by just swapping groups

# map song ordering to then a new playlist



spot.user_playlist_replace_tracks(user, playlist_id, tracks)