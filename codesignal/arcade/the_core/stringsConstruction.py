from collections import Counter

def stringsConstruction(a, b):
    ad = Counter(a)
    bd = Counter(b)
    return min([bd[c]//ad[c] for c in ad])

