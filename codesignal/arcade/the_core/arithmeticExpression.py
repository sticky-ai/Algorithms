def arithmeticExpression(a, b, c):
    try_list = [a + b == c, a - b == c, a * b == c, a / b == c]
    return True in try_list

