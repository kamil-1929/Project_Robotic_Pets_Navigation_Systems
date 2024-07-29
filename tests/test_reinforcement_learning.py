import unittest
from lib.reinforcement_learning import train_rl_agent, evaluate_rl_agent
from lib.config import GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES

class TestReinforcementLearning(unittest.TestCase):
    def test_train_rl_agent(self):
        Q = train_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, [])
        self.assertIsInstance(Q, dict, "Q should be a dictionary")

    def test_evaluate_rl_agent(self):
        path = evaluate_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, [])
        self.assertGreater(len(path), 0, "Path should have at least one step")
        self.assertEqual(path[0], START_POS, "Path should start at the start position")
        self.assertEqual(path[-1], GOAL_POS, "Path should end at the goal position")

if __name__ == '__main__':
    unittest.main()
