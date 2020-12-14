def digitDegree(n):
    cnt = 0
    while n >= 10:
        cnt += 1
        n = sum(int(i) for i in str(n))
        print(n)
    return cnt
