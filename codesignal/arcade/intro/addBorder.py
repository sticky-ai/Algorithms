def addBorder(picture):
    lst = []

    lst.append("*"*(len(picture[0])+2))
    for i in picture:
        i = "*" + i + "*"
        lst.append(i)
    lst.append("*"*(len(picture[0])+2))
    
    return lstad
