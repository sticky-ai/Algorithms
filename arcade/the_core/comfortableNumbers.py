from itertools import combinations

def comfortableNumbers(l, r):
    cnt = 0
    arr = []
    for a, b in combinations(range(l, r+1), 2):
        if is_comfortable(a, b) and is_comfortable(b, a):
            cnt += 1
    return cnt
    
def is_comfortable(a, b):
    s = sum([int(i) for i in str(a)])
    return a - s <= b <= a + s
