def differentSquares(m):
    group = []
    for r in range(len(m) - 1):
        for c in range(len(m[0]) - 1):
            matrix = [m[r][c], m[r][c+1], m[r+1][c], m[r+1][c+1]]
            group.append(matrix)
    
    answer = []
    for g in group:
        if g not in answer:
            answer.append(g)
    
    return len(answer)

    



