def stolenLunch(note):
    c_key = {k:v for k, v in zip('abcdefghij', range(0, 10))}
    n_key = {v:k for k, v in zip('abcdefghij', range(0, 10))}
    
    res = ''
    for n in note:
        if n in c_key.keys():
            res += str(c_key[n])
        elif n in '0123456789':
            res += n_key[int(n)]
        else:
            res += n
    return res
