import numpy as np

class WindyGridWorld:
    def __init__(self, width, height, wind_strength):
        self.width = width
        self.height = height
        self.wind = np.array(wind_strength)
        self.start = (3, 0)
        self.goal = (3, 7)
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def move(self, state, action):
        r, c = state
        dr, dc = self.actions[action]
        new_r = min(max(r + dr + self.wind[c], 0), self.height - 1)
        new_c = min(max(c + dc, 0), self.width - 1)
        return (new_r, new_c), -1 if (new_r, new_c) != self.goal else 0

    def is_terminal(self, state):
        return state == self.goal
