from itertools import combinations

def tripletSum(x, a):
    for c in set(combinations(a, 2)):
        diff = x - sum(c)
        if diff not in c:
            if diff in a:
                return True
    return False
