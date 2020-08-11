def evenDigitsOnly(n):
    return sum([1 for i in str(n) if int(i) % 2 != 0]) == 0

