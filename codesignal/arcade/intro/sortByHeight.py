def sortByHeight(a):

    lst = sorted([i for i in a if i > 0])
    err_lst = [i for i in range(len(a)) if a[i] == -1]

    for i in err_lst:
        lst.insert(i, -1)

    return lst
