def pagesNumbering(n):
    return sum(len(str(i)) for i in range(1, n+1))
