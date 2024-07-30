import unittest
from lib.visualize import visualize_paths

class TestVisualize(unittest.TestCase):
    def test_visualize_paths(self):
        initial_path = [(0, 0), (0, 1), (0, 2), (0, 3)]
        final_paths = [
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(0, 0), (0, 1), (0, 2), (1, 2)],
            [(0, 0), (0, 1), (1, 1), (1, 2)]
        ]
        
        try:
            last_frame_path, gif_path = visualize_paths(initial_path, final_paths, interval=1)
        except Exception as e:
            self.fail(f"visualize_paths raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()

