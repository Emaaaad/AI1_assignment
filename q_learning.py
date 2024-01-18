import numpy as np


def q_learning(env, num_episodes, alpha, gamma, epsilon):
    q_values = np.zeros((env.height, env.width, len(env.actions)))
    for _ in range(num_episodes):
        state = env.start
        while not env.is_terminal(state):
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(len(env.actions))  # Explore
            else:
                action = np.argmax(q_values[state])  # Exploit

            next_state, reward = env.move(state, action)
            q_values[state][action] += alpha * (reward + gamma * np.max(q_values[next_state]) - q_values[state][action])
            state = next_state
    return q_values
