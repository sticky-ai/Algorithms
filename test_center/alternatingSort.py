def alternatingSort(a):
    c,l = 0, a[0]
    while c != (len(a)-1) // 2:
        c =- c if c < 0 else -c - 1
        if a[c] <= l:
            return False
        l = a[c]
    return True
