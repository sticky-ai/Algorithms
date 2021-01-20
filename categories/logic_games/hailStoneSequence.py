def hailstoneSequence(n):
    cnt = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cnt += 1
    return cnt
