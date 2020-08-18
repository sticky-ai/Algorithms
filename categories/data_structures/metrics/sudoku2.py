import numpy as np

def sudoku2(grid):
    def checkRow(grid):
        for g in grid:
            p = re.findall('[0-9]', ''.join(g))
            if len(p) != len(set(p)):
                return False
        return True
    
    def checkColumn(grid):
        for g in zip(*grid):
            print(g)
            p = re.findall('[0-9]', ''.join(g))
            if len(p) != len(set(p)):
                return False
        return True
        
    def checkGrid(grid):
        grid = np.array(grid)
        for i in range(0, len(grid), 3):
            for j in range(0, len(grid[0]), 3):
                p = re.findall('[0-9]', ''.join(grid[i:i+3, j:j+3].flatten()))
                if len(p) != len(set(p)):
                    return False
        return True
    
    return all([checkRow(grid), checkColumn(grid), checkGrid(grid)])
