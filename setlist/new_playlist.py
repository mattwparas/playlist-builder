from get_data import *
from save_data import *
import os

# print(os.environ)


# Design flow

# Get the playlist information
# Remove all the songs from the playlist
# Assign grouping and ordering within that group
# Shuffle those groups from a high level
# Put shuffled music back into the playlist with the new ordering


SPOTIPY_CLIENT_ID = os.environ['MY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['MY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

# scope = 'playlist-modify-public'
username = "frog_bird"
playlist_name = "DM"
scope = 'playlist-read-private'

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

playlistid, spot = get_playlist_id(token, username, playlist_name)

# get tracks from the playlist first
tracklist = get_playlist_tracks(username, playlistid, spot)

features = get_features(tracklist, spot)

save_to_json("features.json", features)

# remove playlist tracks
print(features[0])

print(len(features))

# make recursive mark down thing for ethan

# JSON

# keep dictionary of ID -> group number
# keep dictionary of group number -> [id, id, id, id]
# keep ordering easily, by just swapping groups

# map song ordering to then a new playlist



# spot.user_playlist_replace_tracks(user, playlist_id, tracks)