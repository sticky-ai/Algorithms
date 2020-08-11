def correctNonogram(s, nomo):
    n_cells = int((s + 1) / 2)
    
    grid = [nomo[i][n_cells:] for i in range(n_cells, len(nomo))]
    r_nums = [list(map(str, map(len, [n for n in ''.join(g).split('.') if n != '']))) for g in grid]
    c_nums = [list(map(str, map(len, [n for n in ''.join(g).split('.') if n != '']))) for g in zip(*grid)]
    
    left = [(n_cells - len(r_nums[i])) * ['-'] + r_nums[i] + grid[i] for i in range(len(grid))]
    up = [['-'] * n_cells + u for u in map(list, zip(*[(n_cells - len(c)) * ['-'] + c for c in c_nums]))]
    
    ans = []
    for u in up: ans.append(u)
    for l in left: ans.append(l)
    
    return nomo == ans
