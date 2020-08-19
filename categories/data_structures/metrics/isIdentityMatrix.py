import numpy as np

def isIdentityMatrix(matrix):
    m = np.asarray(matrix)
    i = np.identity(len(matrix))
    return all((m == i).flatten())
