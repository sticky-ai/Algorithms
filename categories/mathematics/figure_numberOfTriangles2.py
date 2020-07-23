def numberOfTriangles2(sticks):
    from itertools import combinations
    cnt = 0
    for c in combinations(sticks, 3):
        c = list(c)
        maxLen = c.pop(c.index(max(c)))
        if maxLen < sum(c):
            cnt += 1
    return cnt
