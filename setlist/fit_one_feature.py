# import stuff
import numpy as np
from objective import Fit_Regression
import matplotlib.pyplot as plt
from save_data import *
import os
from get_data import *
from functions import *
from demographics import *


# take as an input, some continuous function that can then be
# discretized into explicit values

# those are then "buckets" that are held at each point that the
# values from the playlist are going to fit

# iterate through and select closest matching via distance matrix


# given user defined function

# discrete_sin(35, min_value = 0.3, show_plot=True)


feature_list = open_file("features.json")

feature_values = [x for x in feature_list if x is not None]

playist_length = len(feature_values)

# user_function = np.random.uniform(low = 0.3, size = playist_length)
# sin
# user_function = discrete_sin(playist_length, 4, min_value=0.5, max_value=0.9)

# user_function = discrete_beta(playist_length, 2, 6, min_value=0.5, max_value=0.9)

user_function = discrete_normal(playist_length, min_value=.6, max_value=.95)

# feature_hist('energy', feature_values)

# discrete_beta(50, 2, 6, min_value=0.3, max_value=.8, show_plot=True)
# discrete_normal(50, min_value=.5, max_value=.9, show_plot=True)

# user_function = np.linspace(.3, 1, num = playist_length)

single_fit = Fit_Regression(feature_values, 'energy', user_function)
single_fit.perform_swaps()
single_fit.pprint()
single_fit.graph_results()

uris = [x['uri'] for x in single_fit.reordered_features]

print(uris)


# SPOTIPY_CLIENT_ID = os.environ['MY_CLIENT_ID']
# SPOTIPY_CLIENT_SECRET = os.environ['MY_CLIENT_SECRET']
# SPOTIPY_REDIRECT_URI = 'http://localhost:8888/'

# username = "frog_bird"
# playlist_name = "Anything But Christmas 2.0"
# scope = 'playlist-read-private'

# token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
#                                    client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

# playlistid, spot = get_playlist_id(token, username, playlist_name)


# if playist_length <= 100:
#     spot.user_playlist_replace_tracks(username, playlistid, uris)
# else:
#     spot.user_playlist_add_tracks(username, playlistid, uris[0:100])
#     spot.user_playlist_add_tracks(username, playlistid, uris[100:])
