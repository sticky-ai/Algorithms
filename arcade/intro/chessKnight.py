def chessKnight(cell):
    count = 0
    pos = [ord(cell[0]) - 96, int(cell[1])]
    rule = [[1,2], [2,1], [1,-2], [-2,1], [-1,2], [2,-1], [-1,-2], [-2,-1]]

    for i in rule:
        if 0 < pos[0] + i[0] < 9 and 0 < pos[1] + i[1] < 9:
            count += 1
    return count
