# game-of-life
 Python implementation of Conway's Game of Life

# Getting started
 To install the required packages run `pip install -r requirements.txt` from the project's directory

 Starting the game is as simple as running `life.py`.
 
 Specific patterns can be loaded using the `-p` or `--pattern` argument. For example, a blinker can be ran using: 
 ```
 python life.py -p blinker
 ```
 A dictionary containing all implemented patterns can be found in `life.py`.
 
 Additionally, the starting dimensions of the grid can also be set using `--height` or `-w` and `--weight`.
