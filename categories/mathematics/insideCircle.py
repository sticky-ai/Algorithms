def insideCircle(point, center, radius):
    cx, cy, px, py = *center, *point
    return math.sqrt((cx - px) ** 2 + (cy - py) ** 2) <= radius
