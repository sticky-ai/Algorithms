from fractions import gcd

def countBlackCells(n, m):
    if n == m:
        return 3 * n - 2
    else:
        return n + m + gcd(m, n) - 2
    
