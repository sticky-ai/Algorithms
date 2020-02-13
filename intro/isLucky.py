def isLucky(n):
    a = str(n)
    half = int(len(a)/2)
    fa = a[0:int(half)]
    la = a[int(half):]

    result1 = 0
    result2 = 0
    for i in fa: result1 += int(i)
    for i in la: result2 += int(i)
        
    return result1 == result2
