def alternatingSums(a):
    lst = []
    lst2 = []
    result = []
    for i in range(len(a)):
        if i==0 or i%2 == 0:
            lst.append(a[i])
        else:
            lst2.append(a[i])
    
    result.append(sum(lst))
    result.append(sum(lst2))
    
    return result
