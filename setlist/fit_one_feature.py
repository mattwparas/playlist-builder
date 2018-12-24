# import stuff
import numpy as np
from objective import Fit_Regression
import matplotlib.pyplot as plt



# take as an input, some continuous function that can then be 
# discretized into explicit values

# those are then "buckets" that are held at each point that the
# values from the playlist are going to fit

# iterate through and select closest matching via distance matrix


# given user defined function

# discretize
playlist_length = 35
playlist_feature_list = np.random.uniform(low = 0.3, size = playlist_length)
user_function = np.random.uniform(low = 0.3, size = playlist_length)
# user_function = np.array([0.5, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.6, 0.8])

single_fit = Fit_Regression(playlist_feature_list, user_function)
single_fit.perform_swaps()
single_fit.pprint()
single_fit.graph_results()







