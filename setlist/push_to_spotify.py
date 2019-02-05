SPOTIPY_CLIENT_ID = os.environ['MY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['MY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

username = "frog_bird"
playlist_name = "Test Groove"
scope = 'playlist-read-private'

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

playlistid, spot = get_playlist_id(token, username, playlist_name)

if playist_length <= 100:
	pass
    spot.user_playlist_replace_tracks(username, playlistid, uris)
else:

	batch_size = 100
	number_of_batches = math.floor(playist_length / batch_size)
	print(number_of_batches)

	current_batch = 1
	i = 0
	j = 100

	while current_batch < number_of_batches:
		spot.user_playlist_add_tracks(username, playlistid, uris[i:j])
		i += 100
		j += 100
		current_batch += 1

	if current_batch == number_of_batches and j < playist_length:
		spot.user_playlist_add_tracks(username, playlistid, users[j:])