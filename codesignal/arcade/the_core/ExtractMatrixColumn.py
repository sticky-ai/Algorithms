def extractMatrixColumn(matrix, column):
    return [c for c in zip(*matrix)][column]
