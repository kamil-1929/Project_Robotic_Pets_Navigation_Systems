import random

GRID_SIZE = 10
START_POS = (0, 0)
GOAL_POS = (9, 9)
NUM_STATIC_OBSTACLES = 8

def generate_obstacles(grid_size, start_pos, goal_pos, num_obstacles):
    obstacles = set()
    while len(obstacles) < num_obstacles:
        obstacle = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        if obstacle != start_pos and obstacle != goal_pos:
            obstacles.add(obstacle)
    return list(obstacles)

STATIC_OBSTACLES = generate_obstacles(GRID_SIZE, START_POS, GOAL_POS, NUM_STATIC_OBSTACLES)
DYNAMIC_OBSTACLES = []

