def isIPv4Address(inputString):
    splt = inputString.split('.')

    if len(splt) is not 4:
        return False

    for i in splt:
        if i.isdigit() is False:
            return False
        else:
            if 0 <= int(i) <= 255:
                continue
            else:
                return False
    else:
        return True
    
