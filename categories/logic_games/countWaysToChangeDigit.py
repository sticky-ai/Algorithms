def countWaysToChangeDigit(value):
    return sum(9 - int(n) for n in str(value))
