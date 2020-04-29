def isCryptSolution(crypt, solution):
    my_dict = dict(solution)
    
    trans = []
    for word in crypt:
        temp = ''
        for char in word:
             temp += my_dict[char]
        trans.append(temp)

    if trans[0] == '0' and trans[1] == '0':
        return int(trans[0]) + int(trans[1]) == int(trans[2])

    elif trans[0][0] == '0' or trans[1][0] == '0' or trans[2][0] == '0':
        return False
    
    return int(trans[0]) + int(trans[1]) == int(trans[2])

