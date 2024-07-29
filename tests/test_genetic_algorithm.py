import unittest
from lib.genetic_algorithm import genetic_algorithm
from lib.config import GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES

class TestGeneticAlgorithm(unittest.TestCase):
    def test_genetic_algorithm(self):
        initial_path = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)]
        refined_path, best_fitness = genetic_algorithm(initial_path, START_POS, GOAL_POS, STATIC_OBSTACLES, [])
        
        self.assertIsNotNone(refined_path, "Refined path should not be None")
        self.assertGreaterEqual(best_fitness, 0, "Best fitness should be non-negative")

if __name__ == '__main__':
    unittest.main()
