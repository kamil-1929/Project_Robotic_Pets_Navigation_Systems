from lib.config import GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES
from lib.a_star import a_star_search
from lib.reinforcement_learning import train_rl_agent, evaluate_rl_agent
from lib.visualize import visualize_paths
import numpy as np

if __name__ == "__main__":
    # Initialize the grid and obstacles
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for obstacle in STATIC_OBSTACLES:
        grid[obstacle] = 1

    # Print the obstacles for debugging purposes
    print("Static Obstacles:", STATIC_OBSTACLES)

    # Find the initial path using A*
    initial_path = a_star_search(START_POS, GOAL_POS, grid)
    print("Initial Path (A*):", initial_path)

    # Train the Reinforcement Learning agent and get Q-values
    Q = train_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES)

    # Evaluate the RL agent and get the final paths for multiple iterations
    final_paths = []
    for _ in range(10):  # Assuming you want to capture 10 different states for the GIF
        final_path = evaluate_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES)
        final_paths.append(final_path)
    print("Final Paths (Reinforcement Learning):", final_paths)

    # Visualize the paths
    last_frame_path, gif_path = visualize_paths(initial_path, final_paths)
    print(f"Last frame saved as: {last_frame_path}")
    print(f"GIF saved as: {gif_path}")







