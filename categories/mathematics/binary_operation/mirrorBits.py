def mirrorBits(a):
    return int(str(bin(a))[2:][::-1], 2)
