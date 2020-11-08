def countElements(inputString):
    elements = eval(inputString.replace('t', 'T').replace('f', 'F'))
    cnt = 0
    
    if type(elements) is not list:
        return 1
    
    for e in elements:
        if type(e) is list:
            cnt += countElements(str(e))
        else:
            cnt += 1
    
    return cnt
