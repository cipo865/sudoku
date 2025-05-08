from CSP import Sudoku 
from InputOutput import * 
from Heuristics import *
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=True, help='select an input file')
parser.add_argument('-d', '--delay', type=float, default=0, help='specify a delay (in seconds) between printed steps')
parser.add_argument('-H', '--heuristics', action='store_true', help='use the mrv and lcv heuristics')
parser.add_argument('-a', '--ac3', action='store_true', help='use the ac3 constraints propagation')




args = parser.parse_args()
input_file = args.input
delay = args.delay
heuristics = args.heuristics
c_prop = args.ac3
nodes = 0

def next_cell(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return False

def is_valid(sudoku, row, col, num):
    for r, c in sudoku.constraints[row][col]:
        if num == sudoku.grid[r][c]:
            return False
    return True

def back_track(sudoku):
    global nodes
    nodes += 1
    iterative_print(sudoku.grid, nodes, delay)
    cell = mrv(sudoku) if heuristics else next_cell(sudoku.grid)
    if not cell:
        return True
    r, c = cell
    dom = lcv(sudoku, r, c) if heuristics else [num for num in sudoku.domains[r][c]]
    for num in dom:
        old_domains = sudoku.copy_domains()
        sudoku.grid[r][c] = num
        if sudoku.forward_checking(r, c, num):
            if back_track(sudoku):
                return True
        sudoku.domains = old_domains
        sudoku.grid[r][c] = 0
        iterative_print(sudoku.grid, nodes, delay)
    return False

def solve(sudoku):
    if c_prop:
        if not sudoku.ac3():
            print('\nThe provided sudoku was impossible to solve')
            exit()
    if not back_track(sudoku):
        print('\nThe provided sudoku was impossible to solve')
        exit()


def main():
    try:
        grid = load_grid(input_file) 
    except FileNotFoundError:
        print(f'Failed to open {input_file}: file not found')
        exit()
    except LengthException:
        print(f'Failed to open {input_file}: incorrect file length')
        exit()
    except ValueError:
        print(f'Failed to open {input_file}: incorrect file values')
        exit()
    sudoku = Sudoku(grid)
    print('Loaded sudoku:\n')
    fancy_print(grid)
    input('\nPress any key to start solving the sudoku\n')
    start = time.time()
    solve(sudoku)
    elapsed = time.time() - start
    print(f'Sudoku solved in {elapsed} seconds')

if __name__ == "__main__":
    main()