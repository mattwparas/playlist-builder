# playlist-builder

A helpful tool to aid in reordering your Spotify playlists!

## What is playlist-builder?

Have you ever had to put together a playlist for a party? Or maybe for getting amped up? Did you ever feel like the shuffle from Spotify let you down? That you had to skip one too many songs because it didn't fit the mood you wanted at that very moment?

That's where playlist-builder comes in.

Spotify has all sorts of calculated metrics for songs, including 'energy', 'danceability', or 'valence'. Using these metrics, playlist-builder lets you take a playlist, and define a custom function for the flow of your playlist. No more relying on Spotify to shuffle and randomly pick what you want- playlist-builder will reorder the songs in your playlist to best fit the given function.

Essentially, you can define the flow of your night.

## How to use it

In order to use playlist-builder you need to obtain a Spotify Developer Client ID and Secret (look at Spotipy's docs for help with this if you need it).

Once you obtain a client secret and client ID you can then begin fitting your playlist to a generated function.

See example.py to see example usage:

```python
import os
from get_data import *
from functions import *

SPOTIPY_CLIENT_ID = os.environ['MY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['MY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

username = "frog_bird" # your username here
playlist_name = "Test Playlist" # your playlist name here
scope = 'playlist-read-private' # adjust scope as needed, see spotipy docs

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
```

## Fitting Functions

demographics.py includes plotting functions that let you understand the demographics of the playlist that you are working with. For example, here is a generated histogram for the energy levels within a playlist:

<p align="center">
  <img src="images/energyhist.png" width="70%">
</p>

You can also see how the energy level of your playlist changes over time if you were to play it from start to finish:

<p align="center">
  <img src="images/energyvstrack.png" width="70%">
</p>

We can then generate functions to then "fit" the playlist to. For instance, here is an example of a generated sin curve:

<p align="center">
  <img src="images/sinewave.png" width="70%">
</p>

We can then reorder the playlist to fit this function as such:

![AltText](images/fittedcurve.png "Title")

At this point we can then send the playlist back to Spotify to reorder your playlist.

Note, this will remove all of your metadata associated with the songs (i.e. date added to playlist). If this is important to you, push the new changes to a different playlist.




