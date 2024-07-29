import matplotlib.pyplot as plt
import numpy as np
import os
from config import GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES

def visualize_paths(initial_path, refined_path, final_path):
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for obstacle in STATIC_OBSTACLES:
        grid[obstacle] = 1

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.title("Initial Path (A*)")
    grid_with_path = np.copy(grid)
    for pos in initial_path:
        grid_with_path[pos[0], pos[1]] = 0.5
    plt.imshow(grid_with_path, cmap='gray')
    plt.plot([pos[1] for pos in initial_path], [pos[0] for pos in initial_path], 'bo-')
    plt.scatter(START_POS[1], START_POS[0], c='green', s=100, label='Start')
    plt.scatter(GOAL_POS[1], GOAL_POS[0], c='red', s=100, label='Goal')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.title("Refined Path Genetic Algorithm (GA)")
    grid_with_path = np.copy(grid)
    for pos in refined_path:
        grid_with_path[pos[0], pos[1]] = 0.5
    plt.imshow(grid_with_path, cmap='gray')
    plt.plot([pos[1] for pos in refined_path], [pos[0] for pos in refined_path], 'bo-')
    plt.scatter(START_POS[1], START_POS[0], c='green', s=100, label='Start')
    plt.scatter(GOAL_POS[1], GOAL_POS[0], c='red', s=100, label='Goal')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.title("Final Path Reinforcement Learning (RL)")
    grid_with_path = np.copy(grid)
    for pos in final_path:
        grid_with_path[pos[0], pos[1]] = 0.5
    plt.imshow(grid_with_path, cmap='gray')
    plt.plot([pos[1] for pos in final_path], [pos[0] for pos in final_path], 'bo-')
    plt.scatter(START_POS[1], START_POS[0], c='green', s=100, label='Start')
    plt.scatter(GOAL_POS[1], GOAL_POS[0], c='red', s=100, label='Goal')
    plt.legend()

    # Ensure the directory exists
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'visualizations')
    os.makedirs(output_dir, exist_ok=True)

    # Save the figure
    output_path = os.path.join(output_dir, 'paths.png')
    plt.savefig(output_path)
    plt.show()
