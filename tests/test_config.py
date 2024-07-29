import unittest
from lib.config import generate_obstacles, GRID_SIZE, START_POS, GOAL_POS

class TestConfig(unittest.TestCase):
    def test_generate_obstacles(self):
        obstacles = generate_obstacles(GRID_SIZE, START_POS, GOAL_POS, 8)
        self.assertEqual(len(obstacles), 8, "There should be exactly 8 obstacles")
        self.assertNotIn(START_POS, obstacles, "Start position should not be in obstacles")
        self.assertNotIn(GOAL_POS, obstacles, "Goal position should not be in obstacles")

if __name__ == '__main__':
    unittest.main()
