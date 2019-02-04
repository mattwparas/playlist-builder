from get_data import *
from save_data import *
import os
import os.path

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

tracklist = [x for x in tracklist if x is not None]

features = get_features(tracklist, spot)

features = [x for x in features if x is not None]

if features:
	print("Successfully acquired feature information!")

if tracklist:
	print("Successfully acquired tracklist information!")

files_to_remove = ['features.json', 'tracklist.json']

for path in files_to_remove:
	path = 'saved_playlists/' + path
	if os.path.exists(path):
		print("The file", path, "does exist")
		os.remove(path)
	else:
	    print("The file,", path, "does not exist")
	    print("Saving to", path)


save_to_json("saved_playlists/features.json", features)

save_to_json("saved_playlists/tracklist.json", tracklist)



