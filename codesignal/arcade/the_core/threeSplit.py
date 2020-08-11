from itertools import product

def threeSplit(a):

    s = sum(a) // 3
    foo = [sum(a[:i+1]) for i in range(len(a))]
    bar = [i for i in range(len(a) - 2) if foo[i] == s]
    answer = [foo[i+1:-1].count(2 * s) for i in bar]
    return sum(answer)
    
    """ Time Limitation
    prod = product(range(len(a) - 1), repeat = 3)
    perms = [i for i in prod if sum(i) == len(a) and i.count(0) == 0]
    ans = [0 for f, s, t in perms if sum(a[:f]) == sum(a[f:f+s]) == sum(a[f+s:f+s+t])]
    return len(ans) """
