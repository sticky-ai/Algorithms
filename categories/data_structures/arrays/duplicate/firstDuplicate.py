def firstDuplicate(a):
    setter = set()
    for i in a:
        if i in setter:
            return i
        setter.add(i)
    return -1
    
