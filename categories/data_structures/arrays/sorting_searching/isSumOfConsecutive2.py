def isSumOfConsecutive2(n):
    cnt = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if sum(range(i, j)) > n:
                break
            elif sum(range(i, j)) == n:
                cnt += 1
    return cnt
