import numpy as np
import matplotlib.pyplot as plt

# def evaluate_objective(tour, distance_matrix):
#     '''
#     ###############TODO###############

#     Step 1: build distance matrix for transitions
#     Step 2: build dynamic cost as a function of the transitions and their place within the algorithm
#             - this can be some sort of tuning parameter that we assign at the beginning
#             - energy levels, danceability levels - assigned by looking holistically at the entire tour
#     Step 3: Perform preprocessing - separate and combine ideal pairings:
#             - songs that occur on the same album back to back - ideally matched to be back to back
#             - songs that are extremely popular RIGHT NOW (global popularity)
#             - songs that are extremely popular to you individually (local popularity)
#             - 

#     '''
#     # first and last element
#     total_distance = distance_matrix[tour[0], tour[-1]]
#     total_distance = 0
#     for i in range(len(tour) - 1):
#         node1 = tour[i]
#         node2 = tour[i + 1]
#         total_distance += distance_matrix[node1, node2]
#     return total_distance

class Fit_Regression(object):
    def __init__ (self, playlist_feature_list, selected_feature, user_function):
        self.playlist_feature_list = playlist_feature_list
        self.feature = selected_feature
        self.playlist_length = len(playlist_feature_list)
        self.tour = [x for x in range(self.playlist_length)]
        self.user_function = user_function

        distance_matrix = np.zeros((self.playlist_length, self.playlist_length))

        # build distance matrix given songs and user defined function
        for user_index, value in enumerate(user_function):
            for feature_index, feature_dict in enumerate(self.playlist_feature_list):
                distance = abs(value - feature_dict[selected_feature])
                distance_matrix[user_index, feature_index] = distance

        self.distance_matrix = distance_matrix
        self.reordered_features = self.playlist_feature_list
        updated_feature_list = [x[self.feature] for x in self.reordered_features]
        self.residuals = np.array(updated_feature_list) - np.array(self.user_function)

    def evaluate_objective(self):
        '''
        objective for single feature fitting
        '''
        cost = 0
        for index, value in enumerate(self.user_function):
            cost += self.distance_matrix[index, self.tour[index]]

        return cost

    def swaps(self):
        '''
        one iteration of a swap (2-opt)
        '''
        best_tour = self.tour[:]
        best_objective = self.evaluate_objective()
        tour_length = len(self.tour)
        
        for i in range(tour_length):
            for j in range(tour_length):
                node1 = self.tour[i]
                node2 = self.tour[j]
                self.tour[i] = node2
                self.tour[j] = node1
                # Check objective value
                test_objective = self.evaluate_objective()
                # Compare objective values, update accordingly
                if test_objective < best_objective:
                    best_objective = test_objective
                    best_tour = self.tour[:]
                # reset to original ordering
                else:
                    self.tour[i] = node1
                    self.tour[j] = node2
    
    def perform_swaps(self):
        '''
        perform swaps on the tour until the objective value does not change
        '''
        # initialize swaps
        last_objective = self.evaluate_objective()
        best_tour = self.swaps()
        current_objective = self.evaluate_objective()
        while True:
            tour = self.swaps()
            current_objective = self.evaluate_objective()
            if current_objective == last_objective:
                best_objective = current_objective
                best_tour = self.tour[:]
                break
            else:
                last_objective = current_objective

        self.tour = best_tour
        self.reordered_features = [self.playlist_feature_list[x] for x in self.tour]
        updated_feature_list = [x[self.feature] for x in self.reordered_features]
        self.residuals = np.array(updated_feature_list) - np.array(self.user_function)


    def graph_results(self):
        # graph residuals
        plt.figure(figsize=(20, 5))
        # plt.ylim(-.5, .5)
        updated_feature_list = [x[self.feature] for x in self.reordered_features]
        plt.plot(list(range(len(updated_feature_list))), updated_feature_list, '-o')
        plt.plot(list(range(len(self.user_function))), self.user_function, '-o')
        # plt.plot(list(range(len(residuals))), residuals, '-o')
        # plt.ylim(0, 1)
        plt.show()

    def pprint(self):
        print("Objective Value:", self.evaluate_objective())
        print("Tour:", self.tour)




# def evaluate_objective(tour, distance_matrix, user_function):
#     '''
#     objective for single feature fitting
#     '''
#     cost = 0
#     for index, value in enumerate(user_function):
#         cost += distance_matrix[index, tour[index]]

#     return cost

# def swaps(tour, distance_matrix, user_function):
#     '''
#     one iteration of a swap (2-opt)
#     '''
#     best_tour = tour[:]
#     best_objective = evaluate_objective(best_tour, distance_matrix, user_function)
#     tour_length = len(tour)
    
#     for i in range(tour_length):
#         for j in range(tour_length):
#             node1 = tour[i]
#             node2 = tour[j]
#             tour[i] = node2
#             tour[j] = node1
#             # Check objective value
#             test_objective = evaluate_objective(tour, distance_matrix, user_function)
#             # Compare objective values, update accordingly
#             if test_objective < best_objective:
#                 best_objective = test_objective
#                 best_tour = tour[:]
#             # reset to original ordering
#             else:
#                 tour[i] = node1
#                 tour[j] = node2
#     return tour
    
# def perform_swaps(tour, distance_matrix, user_function):
#     '''
#     perform swaps on the tour until the objective value does not change
#     '''
#     # initialize swaps
#     last_objective = evaluate_objective(tour, distance_matrix, user_function)
#     best_tour = swaps(tour, distance_matrix, user_function)
#     current_objective = evaluate_objective(tour, distance_matrix, user_function)
#     while True:
#         tour = swaps(tour, distance_matrix, user_function)
#         current_objective = evaluate_objective(tour, distance_matrix, user_function)
#         if current_objective == last_objective:
#             best_objective = current_objective
#             best_tour = tour[:]
#             break
#         else:
#             last_objective = current_objective

#     return best_tour
