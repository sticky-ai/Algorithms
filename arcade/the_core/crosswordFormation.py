def crosswordFormation(words):
    from itertools import permutations as p
    c = 0
    for l in p(words):
        for d1 in range(len(l[0])-2):
            s1 = [i for i,j in enumerate(l[1]) if j == l[0][d1]]
            for d2 in range(d1+2, len(l[0])):
                s2 = [i for i,j in enumerate(l[2]) if j == l[0][d2]]
                for cw1 in s1:
                    for cw2 in s2:
                        for c1, c2 in zip(l[1][cw1+2:],l[2][cw2+2:]):
                            for c3, c4 in zip(l[3],l[3][d2-d1:]):
                                c += c1 == c3 and c2 == c4
    return c
