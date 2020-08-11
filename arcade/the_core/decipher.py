def decipher(cipher):
    _min, _max = ord('a'), ord('z')
    
    answer = []
    i = 0
    while i < len(cipher):
        if _min <= int(cipher[i:i+3]) <= _max:
            answer.append(cipher[i:i+3])
            i += 3
        else:  
            answer.append(cipher[i:i+2])    
            i += 2
    
    return ''.join([chr(int(i)) for i in answer])
