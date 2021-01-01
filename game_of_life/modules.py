import matplotlib.pyplot as plt
import numpy as np
import random


class GridTooSmall(Exception):
    pass


class Grid:

    MIN_GRID_SIZE = 40
    preset_patterns = {'a': [1]}

    def __init__(self, height=100, width=100, pattern=None):

        if height < Grid.MIN_GRID_SIZE or width < Grid.MIN_GRID_SIZE:
            raise GridTooSmall(f"Height and width should be larger than {Grid.MIN_GRID_SIZE}")

        self.grid = np.zeros((height, width))

        initial_pattern = self._choose_pattern(pattern_choice=pattern)

        self._populate_grid(pattern=initial_pattern)

    def _choose_pattern(self, pattern_choice):

        if pattern_choice is None:
            # Choose an initial pattern at random
            initial_pattern = np.array(random.choice(list(Grid.preset_patterns.values())))

        elif isinstance(pattern_choice, str):
            # Load a specific initial pattern
            initial_pattern = np.array(Grid.preset_patterns[pattern_choice.lower()])

        elif isinstance(pattern_choice, list):
            # Load a manually given pattern
            initial_pattern = np.array(pattern_choice)

        else:
            # Load a random 3x3 pattern
            initial_pattern = np.random.choice([0, 1], size=(3, 3))

        return initial_pattern

    def _populate_grid(self, pattern):

        pattern_shape = pattern.shape

        if len(pattern_shape) == 1:
            pattern_shape = pattern_shape + (1,)
            pattern = pattern.reshape(-1, 1)

        for row in range(pattern_shape[0]):
            for col in range(pattern_shape[1]):
                self.grid[1+row, 1+col] = pattern[row, col]

    def update_grid(self):
        pass

