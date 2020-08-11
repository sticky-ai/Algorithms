def appleBoxes(k):
    yellow = sum([i * i for i in range(k+1) if i % 2 == 1])
    red = sum([i * i for i in range(k+1) if i % 2 == 0])
    return red - yellow
