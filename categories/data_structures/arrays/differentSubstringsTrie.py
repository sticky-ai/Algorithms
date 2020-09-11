from itertools import combinations
def differentSubstringsTrie(inputString):
    cnt = set()
    for i in range(1, len(inputString) + 1):
        for c in combinations(inputString, i):
            if ''.join(c) in inputString:
                cnt.add(c)
    return len(cnt)
