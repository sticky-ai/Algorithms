from collections import defaultdict as D

def proCategorization(A, B):
    d = D(list)
    
    for a, b in zip(A, B):
        for c in b:
            d[c].append(a)
    
    return sorted([[k], v] for k, v in d.items())
