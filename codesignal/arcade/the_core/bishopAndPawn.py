def bishopAndPawn(bishop, pawn):
    position = [abs(ord(pos[0]) - ord(pos[1])) for pos in zip(bishop, pawn)]
    return position[0] == position[1]
