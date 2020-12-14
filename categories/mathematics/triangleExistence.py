def triangleExistence(sides):
    sides.sort()
    return sides[-1] < sum(sides[:-1])
