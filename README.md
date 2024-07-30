# Robotic Pets Navigation Systems

## Overview
This project focuses on developing navigation systems for robotic pets using various algorithms like A* search and Reinforcement Learning. The aim is to provide efficient and effective pathfinding solutions for robotic pets in different environments.

![path_animation](https://github.com/user-attachments/assets/819c27bd-88a6-408d-a0ee-80a092c502c6)


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Algorithms](#algorithms)
  - [A* Search](#a-search)
  - [Reinforcement Learning](#reinforcement-learning)
- [Implementation](#implementation)
  - [A* Search Implementation](#a-search-implementation)
  - [Reinforcement Learning Implementation](#reinforcement-learning-implementation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation
To install the required dependencies, run the following command:
```
pip install -r requirements.txt
```
## Usage

1. Clone the repository:
    ```
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```
    cd x23233982-AIDM_Project_Robotic_Pets_Navigation_Systems-main
    ```
3. Run the main script:
    ```
    python lib/main.py
    ```

## Project Structure
```
x23233982-AIDM_Project_Robotic_Pets_Navigation_Systems-main/
├── .github/
│   └── workflows/
│       └── python-package.yml
├── docs/
│   └── Implementation.txt
├── lib/
│   ├── a_star.py
│   ├── config.py
│   ├── main.py
│   ├── reinforcement_learning.py
│   └── visualize.py
├── outputs/
│   ├── output.txt
│   └── visualizations/
│       └── paths.png
├── tests/
│   ├── __init__.py
│   ├── test_a_star.py
│   ├── test_config.py
│   ├── test_reinforcement_learning.py
│   └── test_visualize.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
## Algorithms

### A* Search
Implemented in `lib/a_star.py`, this algorithm finds the shortest path from the start node to the goal node in a weighted grid.

### Reinforcement Learning
Implemented in `lib/reinforcement_learning.py`, this algorithm trains an agent to navigate the environment through trial and error.

## Implementation

### A* Search Implementation
The A* search algorithm is implemented in the `lib/a_star.py` file. Below are the detailed steps of the implementation:

#### Initialization:
- Import necessary libraries: `heapq` for priority queue operations and `numpy` for matrix operations.
- Define the `Node` class to represent each cell in the grid with attributes like position, parent, g (cost from start to current node), h (heuristic cost from current node to goal), and f (total cost).

#### Heuristic Function:
- Define a heuristic function, typically using the Manhattan distance for grid-based pathfinding.

#### A* Function:
1. Initialize the open and closed lists.
2. Add the start node to the open list.
3. Loop until the open list is empty:
   - Pop the node with the lowest f value.
   - If this node is the goal node, reconstruct the path by tracing back to the start node using parent pointers.
   - Generate the neighboring nodes (up, down, left, right).
   - For each neighbor, calculate the g, h, and f values.
   - If the neighbor is in the closed list and the new path is not better, skip it.
   - If the neighbor is not in the open list or the new path is better, update its values and set its parent to the current node, then add it to the open list.

### Reinforcement Learning Implementation
The Reinforcement Learning (RL) approach is implemented in the `lib/reinforcement_learning.py` file. Below are the detailed steps of the implementation:

#### Initialization:
- Import necessary libraries: `numpy`, `random`, and RL-specific libraries such as `gym` if using OpenAI Gym for environment simulation.
- Define the environment and hyperparameters such as learning rate, discount factor, exploration rate, and number of episodes.

#### Q-Learning Algorithm:
1. Initialize the Q-table with dimensions corresponding to the state and action spaces.
2. For each episode:
   - Reset the environment to get the initial state.
   - Loop until the episode is done:
     - Choose an action based on the exploration-exploitation trade-off.
     - Perform the action in the environment to get the next state, reward, and done flag.
     - Update the Q-value using the Q-learning update rule.
     - Transition to the next state.
   - Optionally, decay the exploration rate.

#### Policy Extraction:
- After training, extract the optimal policy by selecting the action with the highest Q-value for each state.

## Testing
Unit tests are provided to ensure the correctness of the algorithms and can be found in the `tests/` directory. To run the tests, use:
```
pytest
```

## Contributing
Contributions are welcome! Please read the `CONTRIBUTING.md` (if available) for guidelines on how to contribute to this project.
