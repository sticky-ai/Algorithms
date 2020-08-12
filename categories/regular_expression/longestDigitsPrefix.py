def longestDigitsPrefix(inputString):
    p = re.findall('^[0-9]+', inputString)
    return p[0] if len(p) != 0 else ''
