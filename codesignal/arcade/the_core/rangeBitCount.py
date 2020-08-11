def rangeBitCount(a, b):
    nums = list(range(a, b+1))
    to_bin = list(map(bin, nums))
    return sum([i.count('1') for i in to_bin])
