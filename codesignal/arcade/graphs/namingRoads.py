from collections import defaultdict as dd

def namingRoads(roads):
    c = dd(set)
    
    for c1, c2, n in roads:
        c[c1].add(n)
        c[c2].add(n)
    
    for v in c.values():
        for n in v:
            if n-1 in v or n+1 in v:
                return False
    return True
