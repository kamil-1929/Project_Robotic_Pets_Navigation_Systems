# x23233982-AIDM_Project_Robotic_Pets_Navigation_Systems
Project_AIDM_Robotics_Navigating

# Robotic Navigation System

## Overview
This project implements a navigation system for robotic pets using a combination of A* algorithm, and Reinforcement Learning (RL). This hybrid approach ensures efficient initial pathfinding, refined obstacle avoidance, and dynamic adaptation to environmental changes.

## Detailed Implementation and Approach

### A* Algorithm Implementation
The A* algorithm is a popular pathfinding and graph traversal algorithm. It is used to find an initial path from the start position to the goal position while avoiding static obstacles.

**Approach:**
1. **Grid Representation**: The environment is represented as a grid where each cell can be traversable or an obstacle.
2. **Heuristic Function**: The Manhattan distance heuristic is used to estimate the cost from the current node to the goal.
3. **Cost Calculation**: The total cost function `f(n) = g(n) + h(n)` combines the cost to reach the current node `g(n)` and the heuristic estimate `h(n)`.
4. **Pathfinding**: The algorithm explores nodes based on the lowest total cost, updating the path until the goal is reached.

### Reinforcement Learning Implementation
Reinforcement Learning (RL) is employed to dynamically adapt the refined path to handle changes in the environment, especially dynamic obstacles.

**Approach:**
1. **Environment Setup**: The grid environment is defined, including the positions of static and dynamic obstacles.
2. **Q-Learning Agent**: A Q-learning agent is trained to navigate the grid by learning the optimal policy for moving from the start position to the goal.
3. **Reward System**: The agent receives rewards for reaching the goal and penalties for hitting obstacles.
4. **Policy Learning**: The agent updates its Q-values based on the received rewards, aiming to maximize cumulative rewards over time.

### Integration of Algorithms
The overall approach integrates the strengths of A* and RL to create a robust navigation system.

**Workflow:**
1. **Initial Pathfinding**: Use A* to find a quick initial path from the start to the goal, avoiding static obstacles.
2. **Path Refinement** and **Dynamic Adaptation**: Utilize RL to adapt the refined path in real-time, handling dynamic changes in the environment.

**Example Workflow:**
1. **Initial Path (A*)**:
    - Start: (0, 0)
    - Goal: (9, 9)
    - Obstacles: [(1, 2), (2, 2), (3, 2), (4, 2), (5, 5), (6, 6), (7, 7), (8, 8)]

2. **Dynamic Adaptation (RL)**:
    - Q-learning parameters: α = 0.1, γ = 0.99, ε = 0.1
    - Episodes: 1000

## Conclusion
The integration of A* and Reinforcement Learning offers a powerful approach to optimizing robotic pets' navition. This hybrid method ensures efficient initial pathfinding, refined obstacle avoidance, and dynamic adaptation to environmental changes. The provided toy dataset and experimental setup demonstrate the effectiveness of this approach, laying the foundation for further real-world applications and advancements in AI-driven robotic navition systems.

## Installation

To install and run the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/robotic-navigation-system.git
    cd robotic-navigation-system
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the main script:**
    ```bash
    python main.py
    ```

## Usage

1. **Configure the environment:**
    - Edit the `config.json` file to set up the grid environment, obstacles, and algorithm parameters.

2. **Run the algorithms:**
    - Execute the main script to see the navigation system in action.

3. **Visualize the path:**
    - The script will output the initial path, refined path, and dynamically adapted path. Visualizations will be saved in the `output` directory.

## Contribution

We welcome contributions to improve this project. Please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -m "Description of changes"
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-branch
    ```
5. **Create a pull request.**



## Acknowledgements

- Thanks to the open-source community for the libraries and tools used in this project.
- Special thanks to contributors and reviewers for their valuable input and feedback.

