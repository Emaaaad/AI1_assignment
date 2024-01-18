# main.py

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

from environment import WindyGridWorld
from q_learning import q_learning
from visualization import visualize_q_values_on_axes, visualize_policy_table_on_axes


# Create an instance of the environment
wind_strength = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
env = WindyGridWorld(10, 7, wind_strength)

# Parameters
num_episodes = 500
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.1  # exploration rate

# Initialize Q-values
q_values = np.zeros((env.height, env.width, len(env.actions)))

# Run Q-learning and keep track of episode rewards and steps
episode_rewards = []
episode_steps = []
for episode in range(num_episodes):
    total_reward, total_steps = 0, 0
    state = env.start
    while not env.is_terminal(state):
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(len(env.actions))  # Explore
        else:
            action = np.argmax(q_values[state])  # Exploit

        next_state, reward = env.move(state, action)
        total_reward += reward
        total_steps += 1
        q_values[state][action] += alpha * (reward + gamma * np.max(q_values[next_state]) - q_values[state][action])
        state = next_state
    
    episode_rewards.append(total_reward)
    episode_steps.append(total_steps)
    print(f"Episode {episode + 1}: Reward = {total_reward}, Steps = {total_steps}")

print("Training completed.")

# Derive the policy from Q-values
optimal_policy = np.argmax(q_values, axis=2)

# Create a figure and a set of subplots
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(36, 6))  

# Plotting the episode rewards
axs[0].plot(episode_rewards, label='Episode Rewards')
axs[0].set_xlabel('Episodes')
axs[0].set_ylabel('Total Reward')
axs[0].set_title('Total Rewards per Episode')
axs[0].legend()
axs[0].grid(True)

# Plotting the episode steps
axs[1].plot(episode_steps, label='Episode Steps')
axs[1].set_xlabel('Episodes')
axs[1].set_ylabel('Steps taken')
axs[1].set_title('Steps taken per Episode')
axs[1].legend()
axs[1].grid(True)

# Visualize the Q-values as colored squares
visualize_q_values_on_axes(q_values, axs[2])

# Visualize the policy table with colored squares
visualize_policy_table_on_axes(optimal_policy, axs[3])

# Display the plots
plt.tight_layout(pad=3.0)
plt.show()
