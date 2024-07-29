import numpy as np
import gym
from gym import spaces
from collections import defaultdict
import random

class NavigationEnv(gym.Env):
    def __init__(self, grid_size, start_pos, goal_pos, static_obstacles, dynamic_obstacles):
        super(NavigationEnv, self).__init__()
        self.grid_size = grid_size
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.static_obstacles = static_obstacles
        self.dynamic_obstacles = dynamic_obstacles
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=grid_size - 1, shape=(2,), dtype=np.int32)
        self.state = start_pos

    def reset(self):
        self.state = self.start_pos
        return np.array(self.state)

    def step(self, action):
        x, y = self.state
        if action == 0:  # Move up
            x = max(0, x - 1)
        elif action == 1:  # Move down
            x = min(self.grid_size - 1, x + 1)
        elif action == 2:  # Move left
            y = max(0, y - 1)
        elif action == 3:  # Move right
            y = min(self.grid_size - 1, y + 1)

        new_state = (x, y)

        if new_state in self.static_obstacles or new_state in self.dynamic_obstacles:
            reward = -1
            done = True
        elif new_state == self.goal_pos:
            reward = 10
            done = True
        else:
            reward = -0.1
            done = False

        self.state = new_state
        return np.array(self.state), reward, done, {}

    def render(self, mode='human'):
        grid = np.zeros((self.grid_size, self.grid_size))
        for obs in self.static_obstacles:
            grid[obs] = 1
        for obs in self.dynamic_obstacles:
            grid[obs] = 1
        grid[self.goal_pos] = 2
        grid[self.state] = 3
        print(grid)

def train_rl_agent(grid_size, start_pos, goal_pos, static_obstacles, dynamic_obstacles):
    env = NavigationEnv(grid_size, start_pos, goal_pos, static_obstacles, dynamic_obstacles)
    Q = defaultdict(lambda: np.zeros(env.action_space.n))
    alpha = 0.1
    gamma = 0.99
    epsilon = 0.1

    for episode in range(1000):
        state = env.reset()
        done = False
        step_count = 0
        while not done and step_count < 200:  
            if random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[tuple(state)])

            next_state, reward, done, _ = env.step(action)
            best_next_action = np.argmax(Q[tuple(next_state)])
            Q[tuple(state)][action] += alpha * (reward + gamma * Q[tuple(next_state)][best_next_action] - Q[tuple(state)][action])
            state = next_state
            step_count += 1

    return Q

def evaluate_rl_agent(grid_size, start_pos, goal_pos, static_obstacles, dynamic_obstacles):
    env = NavigationEnv(grid_size, start_pos, goal_pos, static_obstacles, dynamic_obstacles)
    Q = train_rl_agent(grid_size, start_pos, goal_pos, static_obstacles, dynamic_obstacles)
    state = env.reset()
    done = False
    path = [start_pos]
    step_count = 0
    while not done and step_count < 200:  # Add a step limit to avoid infinite loops
        action = np.argmax(Q[tuple(state)])
        state, reward, done, _ = env.step(action)
        path.append(tuple(state))
        env.render()
        step_count += 1
    return path
