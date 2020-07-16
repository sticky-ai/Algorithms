def pointInLine(point, line):
    lx, ly, res = line
    px, py = point
    print((lx * px), (ly * py))
    return abs((lx * px) + (ly * py)) == abs(res)
