from itertools import product

def countSumOfTwoRepresentations2(n, l, r):    
    s = set()
    nums = list(range(l, r+1))
    for p in product(nums, nums):
        p = list(p)
        p.sort()
        if sum(p) == n:
            s.add(tuple(p))
    
    return len(s)
