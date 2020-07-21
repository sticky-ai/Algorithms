def findMiddleElement(l):
    m = []
    while l:
        v = l.value
        m.append(v)
        l = l.next
    return m[len(m)//2]
