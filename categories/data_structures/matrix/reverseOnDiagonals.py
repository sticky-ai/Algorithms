import numpy as np

def reverseOnDiagonals(matrix):
    md = np.diag(matrix)
    od = np.diag(np.fliplr(matrix))
    
    for i in range(len(matrix)):
        matrix[i][i] = md[::-1][i]
    
    j = len(matrix[0]) - 1
    for i in range(len(matrix)):
        matrix[i][j] = od[::-1][i]
        j -= 1
    
    return matrix
