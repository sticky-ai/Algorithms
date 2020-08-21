def numberOfTriangles2(sticks):
    from itertools import combinations
    return len([c for c in combinations(sticks, 3) if sum(c) - max(c) > max(c)])
        
