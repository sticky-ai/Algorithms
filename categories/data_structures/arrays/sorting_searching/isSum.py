def isSum(value):
    for i in range(value // 2, 0, -1):
        if sum(range(i)) == value:
            return True
    return False
