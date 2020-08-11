from math import sqrt, ceil

def rectangleRotation(a, b):
    x, y = [ceil(i / sqrt(2)) for i in (a, b)]
    return (x * y) + (x - 1) * (y - 1) - (x + y) % 2
    
