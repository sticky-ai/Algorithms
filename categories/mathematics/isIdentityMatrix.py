import numpy as np

def isIdentityMatrix(matrix):
    return all((matrix == np.identity(len(matrix))).ravel())
    
