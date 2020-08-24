def axisAlignedCirclesBoundingBox(X, Y, R):
    mx, my = [], []
    for x, y, r in zip(X, Y, R):
        mx.append(x - r)
        mx.append(x + r)
        my.append(y - r)
        my.append(y + r)

    return (max(mx) - min(mx)) * (max(my) - min(my))
