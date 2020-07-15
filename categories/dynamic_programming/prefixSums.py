def prefixSums(a):
    ans = []
    x, y = 0, 0
    for n in a:
        x, y = y, y + n
        ans.append(y)
    return ans
