from itertools import product
import numpy as np

def minesweeper(m):
    pos = [p for p in product([-1, 0, 1], [-1, 0, 1]) if p != (0, 0)]
    res = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            cnt = 0
            for p in pos:
                if (i + p[0] >= 0 and i + p[0] < len(m)) and (j + p[1] >= 0 and j + p[1] < len(m[0])):
                    cnt += m[i + p[0]][j + p[1]]
            res.append(cnt)
            
    return np.reshape(res, [len(m), len(m[0])])
