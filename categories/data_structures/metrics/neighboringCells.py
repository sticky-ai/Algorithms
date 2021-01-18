def neighboringCells(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > 0: matrix[i][j] += 1
            if j > 0: matrix[i][j] += 1
            if i + 1 < len(matrix): matrix[i][j] += 1
            if j + 1 < len(matrix[0]): matrix[i][j] += 1
    return matrix
