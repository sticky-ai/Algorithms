def isPowerOfTwo2(n):
    while n > 2:
        if n % 2 != 0:
            return False
        n //= 2
    return True
