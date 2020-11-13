def toAndFro(a, b, t):
    diff = b - a
    q, m = t // diff, t % diff
    if q % 2 == 0:
        return a + m
    return b - m
