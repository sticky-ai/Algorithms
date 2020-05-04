def isSumOfConsecutive2(n):
    c = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if sum(list(range(i, j))) == n:
                c += 1
            elif sum(list(range(i, j))) > n:
                break
    return c
