def sumOfTwo(a, b, v):
    sets = set(b)
    for i in a:
        if (v - i) in sets:
            return True
    return False
    
    """ Solution 1 (Execution Time Limit)
    # sets = [abs(i - v) for i in a]
    # return len([s for s in sets if s in b]) > 0 """

    """ Solution 2 (Execution Time Limit)
    # from itertools import product
    # return v in map(sum, product(a, b)) """
    

