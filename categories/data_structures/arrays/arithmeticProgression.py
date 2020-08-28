def arithmeticProgression(element1, element2, n):
    diff = element2 - element1
    for i in range(n-1):
        element1 += diff
    return element1
