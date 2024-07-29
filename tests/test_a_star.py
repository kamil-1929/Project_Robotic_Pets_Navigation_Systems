import unittest
from lib.a_star import a_star_search
import numpy as np

class TestAStar(unittest.TestCase):
    def test_a_star(self):
        grid = np.zeros((10, 10))
        obstacles = [(1, 2), (2, 2), (3, 2), (4, 2)]
        for obstacle in obstacles:
            grid[obstacle] = 1
        
        start = (0, 0)
        goal = (9, 9)
        path = a_star_search(start, goal, grid)
        
        self.assertIsNotNone(path, "Path should not be None")
        self.assertEqual(path[0], start, "Path should start at the start position")
        self.assertEqual(path[-1], goal, "Path should end at the goal position")

if __name__ == '__main__':
    unittest.main()
