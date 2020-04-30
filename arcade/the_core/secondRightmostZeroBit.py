def secondRightmostZeroBit(n):
    return 2 ** [i for i, num in enumerate(reversed(bin(n)[2:])) if num == '0'][1]

