def weakNumbers(n):
    get_weakness = lambda x: [i for i in range(1, x+1) if x % i == 0]
    d = [len(get_weakness(i)) for i in range(1, n+1)]
    w = [sum(j > m for j in d[:i]) for i,m in enumerate(d)]
    return [max(w), w.count(max(w))]
