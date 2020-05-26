from collections import defaultdict as ddict

def efficientRoadNetwork(n, roads):
    v = ddict(set)

    for r in roads:
        v[r[0]].add(r[1])
        v[r[1]].add(r[0])

    for i in range(n):
        for j in range(i+1, n):
            if i in v[j] or j in v[i] or len(v[i] & v[j]) >= 1:
                continue
            else:
                return False
    return True
