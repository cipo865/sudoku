import sys
import os
import time

first_print = True

def load_grid(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fullname = os.path.join(script_dir, "data/"+filename)
    grid = []
    with open(fullname, 'r') as file:
        for line in file:
            line = [num for num in line.split()]
            if not line or line[0].startswith('#'):
                continue
            line = [int(num) for num in line]
            if len(line) != 9:
                raise LengthException
            grid.append(line)
        if len(grid) != 9:
                raise LengthException
    return grid

def iterative_print(grid, nodes, delay):
    global first_print
    if not first_print:
        sys.stdout.write("\033[15A")
    else:
        first_print = False
    fancy_print(grid)
    print(f'\nExpanded nodes: {nodes}')
    sys.stdout.flush() 
    time.sleep(delay)

def fancy_print(grid):
    for row in range(9):
        if row % 3 == 0:
            print('   -'*13)
        for column in range(9):
            if column % 3 == 0:
                print('   |', end='')
            num = grid[row][column]
            print(f'   {num if num != 0 else "."}', end='')
        print('   |')
    print('   -'*13)
    
class LengthException(Exception):
    def __init__(self):
        super().__init__()
