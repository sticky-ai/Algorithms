def swapDiagonals(matrix):
    d1 = [matrix[i][i] for i in range(len(matrix))]
    d2 = []
    for i in range(len(matrix)):
        j = len(matrix) - i - 1
        d2.append(matrix[i][j])

    for i in range(len(matrix) - 1, -1, -1):
        matrix[i][i] = d2[i]

    for i in range(len(matrix)):
        j = len(matrix) - i - 1
        matrix[i][j] = d1[i]

    return matrix
