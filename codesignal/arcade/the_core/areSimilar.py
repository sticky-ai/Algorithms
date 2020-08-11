def areSimilar(a, b):
    check1 = sum(i != j for i, j in zip(a, b))
    
    return sorted(a) == sorted(b) and check1 in [0, 2]
