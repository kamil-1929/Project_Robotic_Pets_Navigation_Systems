from config import *
from a_star import a_star_search
from reinforcement_learning import train_rl_agent, evaluate_rl_agent
from visualize import visualize_paths
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

    # Simulate dynamically changing paths
    final_paths = []
    for _ in range(10):  
        DYNAMIC_OBSTACLES = generate_obstacles(GRID_SIZE, START_POS, GOAL_POS, NUM_STATIC_OBSTACLES)
        final_path = evaluate_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES)
        final_paths.append(final_path)

    # Visualize the paths as a GIF and PNGs
    last_frame_path, gif_path = visualize_paths(initial_path, final_paths, interval=1)
    print(f"Visualization saved as GIF: {gif_path}")
    print(f"Final Path Saved as PNG: {last_frame_path}")





