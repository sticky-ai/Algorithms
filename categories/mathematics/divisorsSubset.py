def divisorsSubset(subset, n):
    def d(s, n):
        b = False
        for i in range(len(s)):
            b = (n % s[i] == 0)
            if not b:
                return False
        return True
    
    c = 0
    for i in range(1, n+1):
        if d(subset, i):
            c += 1
    return c
