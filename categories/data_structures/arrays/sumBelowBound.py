def sumBelowBound(bound):
    s, i = 0, 1
    while s <= bound:
        s += i
        i += 1
    return i - 2
        
