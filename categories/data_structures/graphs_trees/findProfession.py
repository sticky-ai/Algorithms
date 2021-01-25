def findProfession(level, pos):
    switch = str(bin(pos - 1))[2:]
    p = 0
    
    for i in switch[::-1]:
        if int(i):
            p = 1 - p
    
    if p:
        return 'Doctor'
    else:
        return 'Engineer'

