from lib.config import *
from lib.a_star import a_star_search
from lib.genetic_algorithm import genetic_algorithm
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

    # Refine the path using Genetic Algorithm
    refined_path, best_fitness = genetic_algorithm(initial_path, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES)
    print("Refined Path (GA):", refined_path)
    print("Best Fitness:", best_fitness)

    # Train the Reinforcement Learning agent and get Q-values
    Q = train_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES)

    # Evaluate the RL agent and get the final path
    final_path = evaluate_rl_agent(GRID_SIZE, START_POS, GOAL_POS, STATIC_OBSTACLES, DYNAMIC_OBSTACLES)
    print("Final Path (RL):", final_path)

    # Visualize the paths
    visualize_paths(initial_path, refined_path, final_path)
