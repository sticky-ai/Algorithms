from collections import Counter

def areSimilar(a, b):
    c1, c2 = Counter(a), Counter(b)
    cnt = 0
    for z in zip(c1, c2):
        if z[0] != z[1]:
            cnt += 1
    
    if cnt > 2:
        return False
    else:
        return c1 == c2
