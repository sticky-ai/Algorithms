def digitDifferenceSort(a):
    return sorted(a[::-1], key=lambda x:int(max(str(x))) - int(min(str(x))))
