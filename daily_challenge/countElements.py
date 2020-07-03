def countElements(inputString):
    c = 0
    s = [eval(inputString.replace('t', 'T').replace('f', 'F'))]
    while s:
        obj = s.pop()
        print('list : {}, obj : {}'.format(s, obj))
        if isinstance(obj, list):
            s.extend(obj)
        else:
            c += 1
    return c

