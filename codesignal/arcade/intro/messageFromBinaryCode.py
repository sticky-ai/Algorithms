def messageFromBinaryCode(code):
    split_num = 8
    splited = [code[i*split_num : (i+1)*split_num] for i in range(len(code) // split_num)]
    to_decimal = [int(i, 2) for i in splited]
    to_ascii = list(map(chr, to_decimal))
    decoded = ''.join(to_ascii)
    return str(decoded)
