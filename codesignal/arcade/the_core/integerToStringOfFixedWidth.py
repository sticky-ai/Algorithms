def integerToStringOfFixedWidth(number, width):
    n = str(number)
    if len(n) >= width:
        return n[-width:]
    else:
        return n.zfill(width)
