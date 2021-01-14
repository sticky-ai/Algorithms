def numberOfOperations(a, b):
    cnt = 0
    while math.gcd(a, b) != 1:
        if a % b == 0:
            a //= b
        else:
            b //= a
        cnt += 1
    return cnt

