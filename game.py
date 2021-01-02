import matplotlib.pyplot as plt
import numpy as np
import random


class GridTooSmall(Exception):
    pass


class Grid:

    MIN_GRID_SIZE = 20
    DEFAULT_HEIGHT = 30
    DEFAULT_WIDTH = 30

    preset_patterns = {'blinker': [[0, 0, 0],
                                   [1, 1, 1],
                                   [0, 0, 0]]}

    def __init__(self, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH, pattern=None):

        if height < Grid.MIN_GRID_SIZE or width < Grid.MIN_GRID_SIZE:
            raise GridTooSmall(f"Height and width should be larger than {Grid.MIN_GRID_SIZE}")

        self.cells = np.zeros((height, width))

        initial_pattern = Grid._choose_pattern(pattern_choice=pattern)

        self._populate_grid(pattern=initial_pattern)

    @staticmethod
    def _choose_pattern(pattern_choice):

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
                self.cells[1+row, 1+col] = pattern[row, col]

    def update_grid(self):
        new_grid = self.cells.copy()

        num_rows = new_grid.shape[0]
        num_cols = new_grid.shape[1]

        for row in range(num_rows):
            for col in range(num_cols):

                current_cell = self.cells[row, col]

                num_neighbors = (self.cells[row, (col-1) % num_cols] + self.cells[row, (col+1) % num_cols] +
                                 self.cells[(row-1) % num_rows, col] + self.cells[(row+1) % num_rows, col] +
                                 self.cells[(row-1) % num_rows, (col-1) % num_cols] +
                                 self.cells[(row-1) % num_rows, (col+1) % num_cols] +
                                 self.cells[(row+1) % num_rows, (col-1) % num_cols] +
                                 self.cells[(row+1) % num_rows, (col+1) % num_cols])

                if current_cell == 1 and num_neighbors in [2, 3]:
                    new_cell = 1  # cell survives
                elif current_cell == 0 and num_neighbors == 3:
                    new_cell = 1  # cell survives
                else:
                    new_cell = 0

                new_grid[row, col] = new_cell

        self.cells = new_grid


class Game:

    def __init__(self, grid_height=Grid.DEFAULT_HEIGHT,
                 grid_width=Grid.DEFAULT_WIDTH,
                 init_pattern=None):

        self.grid = Grid(grid_height, grid_width, init_pattern)

    def play(self):
        fig, ax = plt.subplots(1, 1)
        game_state = self.grid.cells
        im = ax.imshow(game_state)

        while True:
            self.grid.update_grid()
            game_state = self.grid.cells
            im.set_data(game_state)
            fig.canvas.draw_idle()
            plt.pause(.25)
