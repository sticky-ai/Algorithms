def axisAlignedBoundingBox(x, y):
    pos = list(zip(*zip(x, y)))
    mx = max(pos[0]) - min(pos[0])
    my = max(pos[1]) - min(pos[1])
    return mx * my
