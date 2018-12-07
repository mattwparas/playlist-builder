
def evaluate_objective(tour, distance_matrix):
    '''
    ###############TODO###############

    Step 1: build distance matrix for transitions
    Step 2: build dynamic cost as a function of the transitions and their place within the algorithm
            - this can be some sort of tuning parameter that we assign at the beginning
            - energy levels, danceability levels - assigned by looking holistically at the entire tour
    Step 3: Perform preprocessing - separate and combine ideal pairings:
            - songs that occur on the same album back to back - ideally matched to be back to back
            - songs that are extremely popular RIGHT NOW (global popularity)
            - songs that are extremely popular to you individually (local popularity)
            - 

    '''
    # first and last element
    total_distance = distance_matrix[tour[0], tour[-1]]
    for i in range(len(tour) - 1):
        node1 = tour[i]
        node2 = tour[i + 1]
        total_distance += distance_matrix[node1, node2]
    return total_distance



def swaps(tour, distance_matrix):
    '''
    one iteration of a swap (2-opt)
    '''
    best_tour = tour[:]
    best_objective = evaluate_objective(best_tour, distance_matrix)
    tour_length = len(tour)
    
    for i in range(tour_length):
        for j in range(tour_length):
            node1 = tour[i]
            node2 = tour[j]
            tour[i] = node2
            tour[j] = node1
            # Check objective value
            test_objective = evaluate_objective(tour, distance_matrix)
            # Compare objective values, update accordingly
            if test_objective < best_objective:
                best_objective = test_objective
                best_tour = tour[:]
            # reset to original ordering
            else:
                tour[i] = node1
                tour[j] = node2
    return tour
    
def perform_swaps(tour, distance_matrix):
    '''
    perform swaps on the tour until the objective value does not change
    '''
    # initialize swaps
    last_objective = evaluate_objective(tour, distance_matrix)
    best_tour = swaps(tour, distance_matrix)
    current_objective = evaluate_objective(tour, distance_matrix)
    while True:
        tour = swaps(tour, distance_matrix)
        current_objective = evaluate_objective(tour, distance_matrix)
        if int(current_objective) == int(last_objective):
            best_objective = current_objective
            best_tour = tour[:]
            break
        else:
            last_objective = current_objective

    return best_tour



def nearest_neighbor(tour, distance_matrix):

    



    return best_tour