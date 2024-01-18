import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


def action_to_arrow(action):
    mapping = {
        0: '↑',  # Up
        1: '↓',  # Down
        2: '←',  # Left
        3: '→'   # Right
    }
    return mapping.get(action, '?')  # Return '?' if action is not in the mapping


def visualize_q_values_on_axes(q_values, ax):
    ax.clear()
    best_q_values = np.max(q_values, axis=2)
    cax = ax.matshow(best_q_values, cmap='viridis')
    cbar = plt.colorbar(cax, ax=ax)
    cbar.ax.set_ylabel('Q-values', rotation=-90, va="bottom")
    ax.set_title('Q-values Heatmap', pad=20)
    ax.set_xlabel('Grid Width')
    ax.set_ylabel('Grid Height')
    ax.set_xticks(np.arange(q_values.shape[1]))
    ax.set_yticks(np.arange(q_values.shape[0]))

def visualize_policy_grade_on_axes(policy, ax):
    ax.clear()
    action_values = {
        0: 0.25,  # Up
        1: 0.50, # Down
        2: 0.75, # Left
        3: 1.0   # Right
    }
    policy_values = np.vectorize(action_values.get)(policy)
    cax = ax.matshow(policy_values, cmap='Pastel1', aspect='equal')

    # Create a color map and normalizer to match the policy values
    cmap = plt.cm.Pastel1
    norm = Normalize(vmin=0.25, vmax=1.0)

    # Create a ScalarMappable and initialize a data structure
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Create the colorbar
    cbar = plt.colorbar(sm, ax=ax, ticks=[0.25, 0.50, 0.75, 1.0])
    cbar.ax.set_yticklabels(['Up', 'Down', 'Left', 'Right'])  # Set text labels
    
    for i in range(policy.shape[0]):
        for j in range(policy.shape[1]):
            action = policy[i, j]
            arrow = action_to_arrow(action)
            ax.text(j, i, arrow, ha='center', va='center', fontsize=12, color='black')

    ax.set_xticks(np.arange(policy.shape[1]) - 0.5, minor=True)
    ax.set_yticks(np.arange(policy.shape[0]) - 0.5, minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.tick_params(axis=u'both', which=u'both', length=0)  # Hide the tick marks
    ax.set_title('Policy Grade Visualization')