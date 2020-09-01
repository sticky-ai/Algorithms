def fractionComparison(a, b):
    A = a[0] * b[1]
    B = a[1] * b[0]
    if A == B:
        return '='
    elif A > B:
        return '>'
    else:
        return '<'
