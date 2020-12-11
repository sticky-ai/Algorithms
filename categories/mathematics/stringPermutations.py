from itertools import permutations

def stringPermutations(s):
    distinct = set()
    for p in map(''.join, permutations(s)):
        distinct.add(p)
    return sorted(distinct)
