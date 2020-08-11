def bishopAndPawn(bishop, pawn):
    char = abs(ord(bishop[0]) - ord(pawn[0]))
    num = abs(int(pawn[1]) - int(bishop[1]))
    return char == num
    

