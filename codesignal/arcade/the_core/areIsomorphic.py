def areIsomorphic(array1, array2):
    r1, r2 = len(array1), len(array2)
    c1, c2 = [len(a1) for a1 in array1], [len(a1) for a1 in array2]
    return r1 == r2 and c1 == c2
