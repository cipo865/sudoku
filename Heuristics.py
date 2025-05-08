def mrv(sudoku): 
    min =10
    cell = False
    for r in range(9):
        for c in range(9):
            if sudoku.grid[r][c] == 0:
                if len(sudoku.domains[r][c]) < min:
                    min = len(sudoku.domains[r][c])
                    cell = (r, c)
    return cell

def lcv(sudoku, row, col):
    return sorted(sudoku.domains[row][col], key=lambda val: sum(val in sudoku.domains[r][c] for r, c in sudoku.constraints[row][col]))
