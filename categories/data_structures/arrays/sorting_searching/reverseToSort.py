def reverseToSort(a):
    for i in range(11):
        for j in range(11):
            t1 = a[:i] + a[i:j][::-1] + a[j:]
            t2 = sorted({*a})
            if t1 == t2:
                return True
    return False
