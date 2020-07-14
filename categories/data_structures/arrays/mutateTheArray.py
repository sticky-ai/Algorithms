def mutateTheArray(n, a):
    a.insert(0, 0)
    a.append(0)
    return [sum(a[i:i+3]) for i in range(n) if len(a[i:i+3]) == 3]
    
