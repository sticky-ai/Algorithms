def zFunctionNaive(s):
    res = []
    for i in range(len(s)):
        c = 0
        for a, b in zip(s[i:], s):
            if a != b:
                break
            c += 1
        res.append(c)
    return res
