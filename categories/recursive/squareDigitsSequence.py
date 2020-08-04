def squareDigitsSequence(a0):
    arr = [a0]
    return div_and_square(a0, arr)
    
def div_and_square(x, arr):
    res = sum([i ** 2 for i in map(int, str(x))])
    if res not in arr:
        arr.append(res)
        return div_and_square(res, arr)
    else:
        return len(arr) + 1


