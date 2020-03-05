def digitsProduct(product):
    if product == 0:
        return 10
    elif product == 1:
        return 1
    
    for i in range(9999):
        total = 1
        for j in str(i):
            total *= int(j)
        if total == product: return i
    return -1
