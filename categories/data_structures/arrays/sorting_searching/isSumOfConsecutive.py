def isSumOfConsecutive(n):
    for i in range(n // 2 + 1, 0, -1):
        s = 0
        for j in range(i + 1, 0, -1):
            s += j 
            if s == n:
                return True
    return False
