def splitAddress(address):
    spl = address.split('://')
    p = spl[0]
    d = spl[1].split('.')[0]
    c = ''
    if len(spl[1].split('.')[1].split('/')) > 1:
        c = spl[1].split('.')[1].split('/')[1]
    
    return [i for i in [p, d, c] if i != '']
