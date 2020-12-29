def possibleSums(coins, quantity):
    v = 0, 
    for c, q in zip(coins, quantity):
        v = {j + i * c for j in v for i in range(q+1)}
    return len(v) - 1
