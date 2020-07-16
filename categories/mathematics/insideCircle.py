def insideCircle(point, center, radius):
    x, y = [z for z in zip(point, center)]
    return math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) <= radius
