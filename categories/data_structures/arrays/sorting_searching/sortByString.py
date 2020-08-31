def sortByString(s, t):
    return ''.join(sorted(s, key=lambda x: t.index(x)))
