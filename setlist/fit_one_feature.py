# import stuff
import numpy as np
from objective import Fit_Regression
import matplotlib.pyplot as plt
from save_data import *
import os
from get_data import *


# take as an input, some continuous function that can then be
# discretized into explicit values

# those are then "buckets" that are held at each point that the
# values from the playlist are going to fit

# iterate through and select closest matching via distance matrix


# given user defined function

def discrete_sin(num_points, periods, min_value=0, show_plot=False):
    Fs = num_points
    f = periods
    sample = num_points
    amplitude = (1 - min_value) / 2
    intercept = 1 - amplitude
    # x = np.linspace(0, sample, num = 34)
    x = np.arange(num_points)
    y = amplitude * np.sin(2 * np.pi * f * x / Fs) + intercept
    if show_plot:
        plt.plot(x, y, '-o')
        plt.show()
    return y


# discrete_sin(35, min_value = 0.3, show_plot=True)


feature_list = open_file("features.json")

feature_values = [x for x in feature_list if x is not None]

playist_length = len(feature_values)

user_function = np.random.uniform(low = 0.3, size = playist_length)
# sin
user_function = discrete_sin(playist_length, 3, min_value=0.3)
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

# scope = 'playlist-modify-public'
# username = "frog_bird"
# playlist_name = "My Test Playlist"
# scope = 'playlist-read-private'

# token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
# client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

# playlistid, spot = get_playlist_id(token, username, playlist_name)

# spot.user_playlist_replace_tracks(username, playlistid, uris)













# unit test here
# discretize
# playlist_length = 35
# playlist_feature_list = np.random.uniform(low = 0.3, size = playlist_length)
# user_function = np.random.uniform(low = 0.3, size = playlist_length)
# # user_function = np.array([0.5, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.6, 0.8])

# single_fit = Fit_Regression(playlist_feature_list, user_function)
# single_fit.perform_swaps()
# single_fit.pprint()
# single_fit.graph_results()
