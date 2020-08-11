def arrayPacking(a):
    return int(''.join(['0' * (8 - len(bin(i)[2:])) + bin(i)[2:] for i in a][::-1]), 2)


