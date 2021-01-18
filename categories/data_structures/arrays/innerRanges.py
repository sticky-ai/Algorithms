def innerRanges(nums, l, r):
    res = []
    for n in [l-1, *nums, r+1]:
        x = n - 1
        if x >= r:
            res += str(r) + f'->{x}' * (x > r), 
        r = n + 1
    return res
