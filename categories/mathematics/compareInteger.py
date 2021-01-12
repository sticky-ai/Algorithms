def compareIntegers(a, b):
    a, b = int(a), int(b)
    if a == b: return 'equal'
    return 'less' if a < b else 'greater'
