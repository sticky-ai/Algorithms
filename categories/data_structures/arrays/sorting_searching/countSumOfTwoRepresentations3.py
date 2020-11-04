def countSumOfTwoRepresentations3(n, l, r):
    s = []
    for i in range(l, r+1):
        for j in range(l, r+1):
            if sum([i, j]) == n:
                s.append(str(sorted([i, j])))
    return len(set(s))
