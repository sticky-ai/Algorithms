def chessKnight(cell):
    p = [ord(cell[0]) - 96, int(cell[1])]
    ways = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
    return len([w for w in ways if 0 < p[0] + w[0] < 9 and 0 < p[1] + w[1] < 9])
    
