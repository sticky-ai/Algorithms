def stringsConstruction(a, b):
    ac, bc = [a.count(n) for n in set(a)], [b.count(n) for n in set(a)] 
    return min([v2 // v1 for v1, v2 in zip(ac, bc)])
