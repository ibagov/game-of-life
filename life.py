from game import Game, Grid
import argparse
import random

# Some pattern generation code taken from http://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/

patterns = {'blinker': [[0, 0, 0],
                        [1, 1, 1],
                        [0, 0, 0]],

            'glider': [[1, 0, 0],
                       [0, 1, 1],
                       [1, 1, 0]],

            'glider_gun': [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                           [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                           [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],

            'r_pentomino': [[0, 1, 1],
                            [1, 1, 0],
                            [0, 1, 0]],

            'spaceship': [[0, 0, 1, 1, 0],
                          [1, 1, 0, 1, 1],
                          [1, 1, 1, 1, 0],
                          [0, 1, 1, 0, 0]],

            'block_switch_engine': [[0, 0, 0, 0, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 0, 1, 1],
                                    [0, 0, 0, 0, 1, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 0, 0, 0],
                                    [0, 0, 1, 0, 0, 0, 0, 0],
                                    [1, 0, 1, 0, 0, 0, 0, 0]]
            }


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--height', help='Height of the grid', type=int, default=Grid.DEFAULT_HEIGHT)
    parser.add_argument('-w', '--width', help='Width of the grid', type=int, default=Grid.DEFAULT_WIDTH)
    parser.add_argument('-p', '--pattern', help='Initial pattern', type=str)
    args = parser.parse_args()

    height = args.height
    width = args.width
    pattern_key = args.pattern

    try:
        init_pattern = patterns[pattern_key]
    except KeyError as e:
        init_pattern = random.choice(list(patterns.values()))

    game = Game(grid_height=height,
                grid_width=width,
                init_pattern=init_pattern)

    game.play()
