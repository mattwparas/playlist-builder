SPOTIPY_CLIENT_ID = # YOUR ID HERE
SPOTIPY_CLIENT_SECRET = # YOUR SECRET HERE
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

scope = 'playlist-read-private'
username = "frog_bird"
playlist_name = "Stone's Birthday Bash"

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

# reset files
files_to_remove = ["testplaylist.json", "featurelist.json", "tracklist.json"]

for path in files_to_remove:
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file,", path, "does not exist")

pid, sp = spt.get_playlist_id(token, username, playlist_name)

tracks = spt.get_playlist_tracks(username, pid, sp)
spt.save_to_json('tracklist.json', tracks)

playlist_uris = [item['track']['uri'] for item in tracks]

feature_list = spt.get_features(tracks, sp)
spt.save_to_json('featurelist.json', feature_list)


data = spt.get_playlist_audio_analysis(playlist_uris, sp)
spt.save_to_json('testplaylist.json', data)