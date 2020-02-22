def variableName(name):
    lst = ['0', '1', '2', '3', '4', '5', 
           '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x',
           'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z', '_']
    

    if name[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
    else:
        if all(i in lst for i in name):
            return True
        else:
            return False


