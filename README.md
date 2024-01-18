# Windy Grid World with Q-Learning

## Project Overview
This project implements a Q-learning agent to solve the Windy Grid World problem, a classical reinforcement learning challenge. The agent learns to navigate through a grid influenced by wind, aiming to reach a goal location in the minimum number of steps. The project demonstrates key concepts of reinforcement learning and Q-learning algorithm, and provides insightful visualizations of the policy and value functions.

**Windy Grid World** is a standard problem in reinforcement learning (RL), a branch of AI where an agent learns to navigate through a grid environment to reach a goal. The unique challenge in this environment is the presence of "wind" in certain columns that pushes the agent upward, affecting its movement and decision-making process.

### Reinforcement Learning and Its Relation to Windy Grid World
Reinforcement Learning is a paradigm where an agent learns to make decisions by performing actions to achieve maximum cumulative reward. Key concepts include the agent, environment, states, actions, and rewards. The agent learns a policy, defining its strategy to choose actions in different states to maximize reward.

In the Windy Grid World:
- The **agent** learns to move from a start state to a goal state on a grid.
- The **environment** includes the grid with certain columns having wind.
- **States** are represented by grid cells, and **actions** include moving up, down, left, or right.
- **Rewards** are given for each action, with penalties for more steps and bonuses for reaching the goal.
- The agent employs RL algorithms like **Q-learning** to learn the value of actions in states, refining its policy to effectively navigate the grid considering the wind's influence.

## Features

- **Windy Grid World Environment**: This project simulates the Windy Grid World, a classic grid-based environment where each cell represents a distinct state. The agent's objective is to navigate from a starting point to a goal location. What makes this environment challenging and unique is the presence of wind in certain columns, which exerts an upward force on the agent, thereby affecting its movement. This necessitates strategic planning and learning by the agent to reach the goal efficiently. The environment is highly customizable, allowing for adjustments in grid size, wind strength, and the placement of start and goal states, making it a versatile tool for studying the nuances of reinforcement learning.

- **Q-Learning Algorithm**: At the heart of the agent's learning process is the Q-learning algorithm, a model-free, off-policy algorithm used in reinforcement learning. This algorithm enables the agent to learn the value of actions in each state, thus developing a policy that guides the agent to take the action with the highest expected reward. Over successive episodes of exploration and learning, the Q-learning algorithm iteratively updates the Q-values based on the rewards received, converging towards an optimal policy that navigates the agent effectively through the windy grid, despite the environmental challenges.

- **Interactive Visualizations**: To provide a clear and intuitive understanding of the agent's learning progress and the effectiveness of the developed policy, this project incorporates two main visualizations:
   - **Q-values Heatmap**: This visualization represents the grid with colors indicating the Q-value of each state. The varying shades provide insights into the potential of each state, guiding the agent's decisions. States with higher Q-values are deemed more desirable, as they are expected to yield higher returns.
   - **Policy Grid Visualization and Arrows**: This intuitive visualization provides a policy overview, with each cell in the grid colored based on the best action to take from that state. Overlaid arrows indicate the direction of the recommended action, offering a quick and informative view of the policy. The combination of color-coding and arrows succinctly demonstrates the strategy learned by the agent, making the policy's dynamics easily understandable.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.6 or later
- Numpy
- Matplotlib

You can install the necessary libraries using pip:
```bash
pip install numpy matplotlib
```

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/Emaaaad/AI1_assignment.git
```
### Usage
Navigate to the project directory and run the main script:
```bash
python3 main.py
```

## Visualizations

The project incorporates sophisticated visual tools to elucidate the learning process and the resulting policy in a visually intuitive manner. These visualizations are pivotal in understanding the complex dynamics of the agent's decision-making process and the environmental challenges it faces.

- **Q-values Heatmap**: This visualization is a cornerstone in illustrating the agent's valuation of each state within the grid. Each cell's color intensity represents the Q-value, which is a measure of the expected utility of taking the best action from that state. A gradient color scheme is employed to depict this, with warmer colors indicating higher Q-values. This heatmap provides a comprehensive view of the agent's learned evaluations, revealing the most promising paths and strategies, as well as the potential pitfalls or less favorable routes. By observing how the Q-values evolve over training episodes, one can gain deep insights into the learning progression and the refinement of the agent's strategy.

![Q-values Heatmap]( https://github.com/Emaaaad/AI1_assignment/blob/master/images/QVH.jpg "Q-values Heatmap")
This heatmap represents the Q-values for each state. States with warmer colors have higher Q-values, indicating they are more promising in terms of expected return. This visualization helps in understanding the agent's assessment of each state's potential.


- **Policy Grid Visualization**: This sophisticated visualization conveys the essence of the learned policy in a direct and interpretable manner. Each cell in the grid is color-coded and contains an arrow; the color signifies the best action to take from that state, and the arrow indicates the direction of the action. This dual coding (color and arrow) offers an immediate, clear understanding of the recommended actions at a glance. For instance, a cell with a specific color and an upward arrow would mean that the best action from that state, according to the learned policy, is to move upwards. This visualization not only serves as a quick reference to the agent's strategy but also illustrates the influence of environmental factors, like wind, on the policy. It's particularly useful for verifying the rationality of the learned policy and for identifying any peculiar behaviors or patterns that might warrant further investigation or optimization.

- 
![Policy Grid Visualization](https://github.com/Emaaaad/AI1_assignment/blob/master/images/PGV.jpg "Policy Grid Visualization")
This grid shows the best action to take from each state, color-coded for clarity, with arrows indicating the direction. It provides an intuitive view of the policy, demonstrating the agent's learned strategy to navigate through the grid effectively, considering the wind's influence.


## Customization
You can adjust the environment and learning parameters in 'main.py' to experiment with different settings and observe how they affect the agent's learning process and performance.
