from itertools import combinations

def countSumOfTwoRepresentations3(n, l, r):
    cnt = 0
    for i in range(l, r+1):
        if i * 2 == n:
            cnt += 1
            
    for c in combinations(range(l, r+1), 2):
        if sum(c) == n:
            cnt += 1
    return cnt 
            
