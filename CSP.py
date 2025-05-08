from collections import deque

class Sudoku:
    def __init__(self, grid):
        self.grid = grid
        self.domains = [[[grid[r][c]] if grid[r][c] != 0 else list(range(1, 10)) for c in range(9)] for r in range(9)]
        self.constraints = self.init_constraints()
        
    def init_constraints(self):
        constraints = []
        for r in range(9):
            line = []
            for c in range(9):
                temp = []
                temp += [(r, col) for col in range(9) if col != c]
                temp += [(row, c) for row in range(9) if row != r]
                temp_r, temp_c = 3 * (r // 3), 3 * (c // 3)
                temp += [(temp_r+tr, temp_c+tc) for tr in range(3) for tc in range(3) if (temp_r+tr != r) and (temp_c+tc != c)]
                line.append(temp)
            constraints.append(line)
        return constraints
    
    def copy_domains(self):
        copy = []
        for r in range(9):
            line = []
            for c in range(9):
                line.append([num for num in self.domains[r][c]])
            copy.append(line)
        return copy

    def ac3(self):
        queue = deque()
        for r in range(9):
            for c in range(9):
                for row, col in self.constraints[r][c]:
                    queue.append(((r, c), (row, col)))
        while queue:
            xi, xj = queue.popleft()
            if self.revise(xi, xj):
                if not self.domains[xi[0]][xi[1]]:
                    return False
                for r, c in self.constraints[xi[0]][xi[1]]:
                    if (r, c) != xj:
                        queue.append(((r, c), xi))
        return True

    def revise(self, xi, xj):
        revised = False
        for valuei in self.domains[xi[0]][xi[1]][:]:  
            has_compatible = False
            for valuej in self.domains[xj[0]][xj[1]]:
                if valuei != valuej:
                    has_compatible = True
                    break
            if not has_compatible:
                self.domains[xi[0]][xi[1]].remove(valuei)
                revised = True
        return revised
    
    def forward_checking(self, row, col, num): 
        for r, c in self.constraints[row][col]:
            if num in self.domains[r][c]:
                self.domains[r][c].remove(num)
                if len(self.domains[r][c]) == 0:
                    return False
        return True
