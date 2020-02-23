def absoluteValuesSumMinimization(a):

    lst = [sum([abs(j - a[i]) for i in range(len(a))]) for j in a]
    min_idx = lst.index(min(lst))
    
    return a[min_idx]
    
    
