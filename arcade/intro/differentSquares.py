def differentSquares(matrix):
    r, c = len(matrix), len(matrix[0])
    sets = set()
    for i in range(r - 1):
        for j in range(c - 1):
                sets.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(sets)
