def arithmeticExpression(a, b, c):
    ops = ['+', '-', '*', '/']
    for op in ops:
        if eval(str(a) + op + str(b)) == c:
            return True
    return False
