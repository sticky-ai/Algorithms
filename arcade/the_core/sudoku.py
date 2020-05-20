def sudoku(grid):
    row_check = [set(r) for r in grid]
    col_check = [set(c) for c in zip(*grid)]
    
    box = []
    for r in range(len(grid)):
        temp = []
        for c in range(len(grid)):
            temp.append(grid[r - r % 3 + c // 3][(r % 3) * 3 + c % 3])
        box.append(temp)
    
    box_check = [set(b) for b in box]
    return all([col_check[i] == row_check[i] == box_check[i] == set(range(1, 10)) for i in range(len(grid))])

