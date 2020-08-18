from itertools import combinations

def maxPairProduct(a):
    s = set()
    for c1, c2 in combinations(a, 2):
        m = c1 * c2
        if m in a:
            s.add(m)
    return max(s) if len(s) != 0 else -1
