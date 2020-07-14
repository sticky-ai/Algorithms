def checker(nums):
    unique = set()
    for i in nums:
        if i == '.':
            continue
        if i in unique:
            return False
        unique.add(i)
    return True

def sudoku2(grid):
    l = len(grid)
    
    for row in grid:
        if checker(row) == False:
            return False
    
    for i in range(l):
        if checker([row[i] for row in grid]) == False:
            return False

    for i in range(0, l, 3):
        for j in range(0, l, 3):
            if not checker(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False

    return True

