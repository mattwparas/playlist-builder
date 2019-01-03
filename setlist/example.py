import os
from get_data import *

SPOTIPY_CLIENT_ID = os.environ['MY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['MY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

# scope = 'playlist-modify-public'
username = "frog_bird" # your username here
playlist_name = "Test Playlist 2" # your playlist name here
scope = 'playlist-read-private' # adjust scope as needed

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

# gets the ID associated with the playlist name and the spotipy object for this token
playlistid, spot = get_playlist_id(token, username, playlist_name)

# get tracks from the playlist first
tracklist = get_playlist_tracks(username, playlistid, spot)

# get features for the playlist
features = get_features(tracklist, spot)

# clean the response
feature_values = [x for x in feature_list if x is not None]

# get the length of the playlist
playist_length = len(feature_values)

# generates a cos wave to fit the songs to
user_function = discrete_cos(playist_length, 4, min_value=0.5)

single_fit = Fit_Regression(feature_values, 'energy', user_function)
single_fit.perform_swaps()
single_fit.pprint()
single_fit.graph_results()

uris = [x['uri'] for x in single_fit.reordered_features]

##### Warning #####
# This will replace all the meta data for the playlist, as it removes all the songs and re adds them
# If this is important to you, seek another method
spot.user_playlist_replace_tracks(username, playlistid, uris)

