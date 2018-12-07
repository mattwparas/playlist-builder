# import sys
# sys.path.append('/Users/mwparas/Documents/PlaylistBuilder/setlist')

import unittest
from objective import evaluate_objective
import numpy as np
import random
# import importlib

size = 10
users = random.shuffle([x for x in range(1, size)])
distance_mat = np.random.rand(size,size)
np.fill_diagonal(distance_mat, 0)

print(distance_mat)

# player_module = importlib.import_module(default_player_path)
# Player = getattr(player_module, 'Player')

# importlib.import_module(path_name)

class PlaylistTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, True)
    def test2(self):
        self.assertEqual(True, True)
    def test3(self):
        self.assertFalse(True == False)

if __name__== "__main__": unittest.main()

