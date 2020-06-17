def chessKnightMoves(cell):
    pos = [ord(cell[0]) - 96, int(cell[1])]
    move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    c = 0
    for x, y in move:
        if pos[0] + x < 1 or pos[0] + x > 8 or pos[1] + y < 1 or pos[1] + y > 8:
            continue
        c += 1
    return c
            
