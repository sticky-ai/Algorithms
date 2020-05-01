def countSumOfTwoRepresentations2(n, l, r):
    if l + r < n:
        l = n - r
    else:
        r = n - l
    
    if l > r:
        return 0
    return (r - l) // 2 + 1

