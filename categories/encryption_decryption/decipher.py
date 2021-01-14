def decipher(cipher):
    i = 0
    arr = []
    for _ in range(len(cipher)):
        try:
            if cipher[i] == '1':
                arr.append(cipher[i:i+3])
                i += 3

            else:
                arr.append(cipher[i:i+2])
                i += 2
        except:
            continue
         
    return ''.join(map(chr, map(int, arr)))
