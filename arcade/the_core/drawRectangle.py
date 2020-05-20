def drawRectangle(canvas, rectangle):
    x1, y1, x2, y2 = rectangle
    canvas[y1][x1], canvas[y1][x2], canvas[y2][x1], canvas[y2][x2] = '*', '*', '*', '*'
    
    for x in range(x1 + 1, x2):
        canvas[y1][x] = '-'
        canvas[y2][x] = '-'
        
    for y in range(y1 + 1, y2):
        canvas[y][x1] = '|'
        canvas[y][x2] = '|'
    
    return canvas
