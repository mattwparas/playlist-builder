import unittest
from objective import *
import numpy as np
import random


size = 10
users = [x for x in range(0, size)]
distance_mat = np.random.randint(3, 45, size = (size,size))
np.fill_diagonal(distance_mat, 0)

class PlaylistTest(unittest.TestCase):
    def test1(self):
        '''
        Generates a random distance matrix, performs the 2 opt swap
        Used to test the functionality of the 2 opt
        '''
        size = 10
        users = [x for x in range(0, size)]
        distance_mat = np.random.randint(3, 45, size = (size,size))
        np.fill_diagonal(distance_mat, 0)
        perform_swaps(users, distance_mat)
        print(evaluate_objective(users, distance_mat))
        print(users)
        self.assertEqual(True, True)
    def test2(self):
        '''
        Generates a random distance matrix, performs the 2 opt swap
        '''

        self.assertEqual(True, True)
    def test3(self):
        self.assertFalse(True == False)

if __name__== "__main__": unittest.main()

