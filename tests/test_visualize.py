import unittest
from lib.visualize import visualize_paths

class TestVisualize(unittest.TestCase):
    def test_visualize_paths(self):
        initial_path = [(0, 1), (0, 2), (0, 3)]
        refined_path = [(0, 1), (0, 2), (0, 3)]
        final_path = [(0, 1), (0, 2), (0, 3)]
        
        try:
            visualize_paths(initial_path, refined_path, final_path)
        except Exception as e:
            self.fail(f"visualize_paths raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
