from functools import reduce

def arrayElementsProduct(inputArray):
    return reduce(lambda x, y: x * y, inputArray)
