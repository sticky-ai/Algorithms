def chessBishopDream(boardSize, initPosition, initDirection, k):
    x = (initPosition[0] + initDirection[0] * k) % (2 * boardSize[0])
    y = (initPosition[1] + initDirection[1] * k) % (2 * boardSize[1])
    if x >= boardSize[0]: 
        x = 2 * boardSize[0] - 1 - x
    if y >= boardSize[1]: 
        y = 2 * boardSize[1] - 1 - y
    return x, y
