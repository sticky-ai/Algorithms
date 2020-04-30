def arrayMaxConsecutiveSum(a, k):
    c = m = sum(a[:k])
    
    for i in range(len(a) - k):
        c += + a[i + k] - a[i]
        m = max(c, m)
        
    return m

