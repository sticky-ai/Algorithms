def reverseOnDiagonals(matrix):
    d1 = [matrix[i][i] for i in range(len(matrix))]
    for i in range(len(matrix) - 1, -1, -1):
        matrix[i][i] = d1[::-1][i]
    
    d2 = []
    for i in range(len(matrix)):
        j = len(matrix) - i - 1
        d2.append(matrix[i][j])

    for i in range(len(matrix)):
        j = len(matrix) - i - 1
        matrix[i][j] = d2[::-1][i]
    
    return matrix
