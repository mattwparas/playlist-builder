# import stuff
import numpy as np
from objective import *
import matplotlib.pyplot as plt



# take as an input, some continuous function that can then be 
# discretized into explicit values

# those are then "buckets" that are held at each point that the
# values from the playlist are going to fit

# iterate through and select closest matching via distance matrix


# given user defined function

# discretize
playlist_length = 10

playlist_feature_list = np.random.uniform(low = 0.3, size = playlist_length)

# user_function = np.random.uniform(size = playlist_length)
user_function = np.array([0.5, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.3, 0.6, 0.8])


distance_matrix = np.zeros((playlist_length, playlist_length))

# build distance matrix given songs and user defined function
for user_index, value in enumerate(user_function):
    for feature_index, feature_value in enumerate(playlist_feature_list):
        distance = abs(value - feature_value)
        distance_matrix[user_index, feature_index] = distance

# perform the swaps necessary
users = [x for x in range(0, playlist_length)]
perform_swaps(users, distance_matrix)
print("Objective Value:", evaluate_objective(users, distance_matrix))
print("Tour:", users)


reordered_features = [playlist_feature_list[x] for x in users]
residuals = abs(np.array(reordered_features) - np.array(user_function))

# graph residuals
plt.figure(figsize=(20, 5))
plt.plot(list(range(len(reordered_features))), reordered_features, '-o')
plt.plot(list(range(len(user_function))), user_function, '-o')
# plt.plot(list(range(len(residuals))), residuals, '-o')
# plt.ylim(0, 1)
plt.show()





