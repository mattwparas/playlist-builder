# import stuff
# import numpy as np
from objective import Fit_Regression
# import matplotlib.pyplot as plt
from save_data import *
import os
from get_data import *
from functions import *
from demographics import *
import math
import time


# save_playlist_information("frog_bird", "DM")


feature_list = open_file("saved_playlists/features.json")

playist_length = len(feature_list)

user_function = discrete_sin(playist_length, 4, min_value=0.5, max_value=0.9)

single_fit = Fit_Regression(feature_list, 'energy', user_function)
single_fit.perform_swaps()
single_fit.pprint()
single_fit.graph_results()

uris = [x['uri'] for x in single_fit.reordered_features]


push_to_playlist(uris, "frog_bird", "testplaylisttest")










