def isLowerTriangularMatrix(matrix):
    p = 1
    for row in matrix:
        for r in row[p:]:
            if r != 0:
                return False
        p += 1
    return True
