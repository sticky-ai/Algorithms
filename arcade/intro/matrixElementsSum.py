def matrixElementsSum(matrix):

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i+1][j] = 0

    return sum([sum(matrix[i]) for i in range(len(matrix))])
