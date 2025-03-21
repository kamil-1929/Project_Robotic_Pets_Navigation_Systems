import matplotlib.pyplot as plt
import numpy as np
import os
import imageio
from lib.config import GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES

def visualize_paths(initial_path, final_paths, interval=1):
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for obstacle in STATIC_OBSTACLES:
        grid[obstacle] = 1

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'visualizations')
    os.makedirs(output_dir, exist_ok=True)

    filenames = []
    for i, final_path in enumerate(final_paths):
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 2, 1)
        plt.title("Initial Path (A*)")
        grid_with_path = np.copy(grid)
        for pos in initial_path:
            grid_with_path[pos[0], pos[1]] = 0.5
        plt.imshow(grid_with_path, cmap='gray')
        plt.plot([pos[1] for pos in initial_path], [pos[0] for pos in initial_path], 'bo-')
        plt.scatter(START_POS[1], START_POS[0], c='green', s=100, label='Start')
        plt.scatter(GOAL_POS[1], GOAL_POS[0], c='red', s=100, label='Goal')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.title("Final Path Reinforcement Learning (RL)")
        grid_with_path = np.copy(grid)
        for pos in final_path:
            grid_with_path[pos[0], pos[1]] = 0.5
        plt.imshow(grid_with_path, cmap='gray')
        plt.plot([pos[1] for pos in final_path], [pos[0] for pos in final_path], 'bo-')
        plt.scatter(START_POS[1], START_POS[0], c='green', s=100, label='Start')
        plt.scatter(GOAL_POS[1], GOAL_POS[0], c='red', s=100, label='Goal')
        plt.legend()

        filename = os.path.join(output_dir, f'frame_{i}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.close()

    # Save the last frame as paths.png
    last_frame_path = os.path.join(output_dir, 'paths.png')
    if os.path.exists(last_frame_path):
        os.remove(last_frame_path)
    os.rename(filenames[-1], last_frame_path)

    # Create a GIF from the saved frames
    gif_path = os.path.join(output_dir, 'path_animation.gif')
    with imageio.get_writer(gif_path, mode='I', duration=interval) as writer:
        for filename in filenames[:-1]:  
            image = imageio.imread(filename)
            writer.append_data(image)
            os.remove(filename)  

    print("GIF saved as 'path_animation.gif'")
    return last_frame_path, gif_path







