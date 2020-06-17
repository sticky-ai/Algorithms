def uniqueDigitProducts(a):
    my_set = set()
    for num in a:
        t = 1
        for n in str(num):
            t *= int(n)
        my_set.add(t)
    return len(my_set)
