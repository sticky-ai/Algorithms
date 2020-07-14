def mergeStrings(s1, s2):
    s, o1, o2= '', s1, s2
    while len(s1) * len(s2) != 0:
        if o1.count(s1[0]) > o2.count(s2[0]) or (o1.count(s1[0]) == o2.count(s2[0]) and s1[0]>s2[0]):
            s += s2[0]
            s2 = s2[1:]
        else:
            s += s1[0]
            s1 = s1[1:]
    return s + s1 + s2
