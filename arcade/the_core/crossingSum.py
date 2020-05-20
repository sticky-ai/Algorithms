def crossingSum(matrix, a, b):
    u1, u2 = matrix[a], [c for c in zip(*matrix)][b]
    return sum(u1) + sum(u2) - matrix[a][b]
