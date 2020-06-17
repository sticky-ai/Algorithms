def whoseTurn(p):
    return sum(map(ord, p)) % 2 == 1
