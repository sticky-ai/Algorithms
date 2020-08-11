def isSubstitutionCipher(s1, s2):
    p1, p2, p3 = set(zip(s1, s2)), set(s1), set(s2)
    return len(p1) == len(p2) == len(p3)
