def crossingSum(matrix, a, b):
    return sum(matrix[a]) + sum(list(zip(*matrix))[b]) - matrix[a][b]
