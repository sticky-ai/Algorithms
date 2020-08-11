from collections import defaultdict

def maximumSum(a, q):
    ddict = defaultdict(int)
    for l, r in q:
        for i in range(l, r + 1):
            ddict[i] += 1
    
    a.sort(reverse = True)
    c = sorted(ddict.values(), reverse = True)
    
    return sum(map(lambda i: c[i] * a[i], range(len(c))))

