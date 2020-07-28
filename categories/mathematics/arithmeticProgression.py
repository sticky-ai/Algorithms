def arithmeticProgression(element1, element2, n):
    if element1 == element2:
        return element1
        
    diff = abs(element1 - element2)
    if element1 > element2:
        diff = -diff
    
    for i in range(n-1):
        element1 += diff
        
    return element1
