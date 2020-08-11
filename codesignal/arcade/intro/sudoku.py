def checker(l):
    return sorted(l) == list(range(1, 10))


def sudoku(grid):
    for i in range(len(grid)):
        if checker(grid[i]) is False: return False
        if checker([grid[x][i] for x in range(0, 9)]) is False: return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if checker([grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]) is False: return False
    return True
