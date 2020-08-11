import re

def isMAC48Address(inputString):
    
    splited = inputString.split('-')
    if len(splited) != 6:
        return False

    try:
        for i in splited:
            if len(i) != 2:
                return False
            int(i, 16)
        return True

    except ValueError:
        return False

