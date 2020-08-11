def sortByHeight(a):
    err_idx = [i for i in range(len(a)) if a[i] == -1]
    nums = sorted([n for n in a if n != -1])
    for e in err_idx:
        nums.insert(e, -1)
    return nums
