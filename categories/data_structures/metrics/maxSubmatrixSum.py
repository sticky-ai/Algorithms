import numpy as np

def maxSubmatrixSum(matrix, n, m):
    mat = np.asarray(matrix)
    
    res = []
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - m + 1):
            res.append(mat[i:i+n, j:j+m])
    
    return max(np.sum(t) for t in res)
