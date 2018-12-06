def evaluate_objective():
    '''
    ###############TODO###############
    '''
    return 1


def swaps(tour):
    '''
    one iteration of a swap (2-opt)
    '''
    best_tour = tour[:]
    best_objective = evaluate_objective(best_tour)
    tour_length = len(tour)
    
    for i in range(1, tour_length):
        for j in range(1, tour_length):
            node1 = tour[i]
            node2 = tour[j]
            
            test_tour = tour[:]
            test_tour[i] = node2
            test_tour[j] = node1
            
            test_objective = evaluate_objective(test_tour)
            
            if test_objective < best_objective:
                best_objective = test_objective
                best_tour = test_tour[:]
    return tour
    
def perform_swaps(tour):
    '''
    perform swaps on the tour until the objective value does not change
    '''
    # initialize swaps
    last_objective = evaluate_objective(tour)
    best_tour = swaps(tour)
    current_objective = evaluate_objective(tour)
    while True:
        swaps()
        test_tour = tour[:]
        current_objective = evaluate_objective(test_tour)
        if int(current_objective) == int(last_objective):
            best_objective = current_objective
            best_tour = test_tour[:]
            break
        else:
            last_objective = current_objective

    return best_tour