import re

def isMAC48Address(inputString):
    p = re.compile('[\dA-F]{2}(-[\dA-F]{2}){5}$')
    return bool(p.match(inputString))
