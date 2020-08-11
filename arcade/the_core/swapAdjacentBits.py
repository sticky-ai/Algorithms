def swapAdjacentBits(n):
    return int(''.join([i[::-1] for i in bit_slicer(n)]), 2)

def bit_slicer(n):
    bits = bin(n)[2:]
    if len(bits) % 2 == 1:
        bits = bits.zfill(len(bits) + 1)

    for i in range(0, len(bits), 2): 
        yield bits[i:i+2]
