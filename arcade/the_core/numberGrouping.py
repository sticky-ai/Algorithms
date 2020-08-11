def numbersGrouping(a):
    groups = set([(n-1) // 10 ** 4 for n in a])
    return len(groups) + len(a)

