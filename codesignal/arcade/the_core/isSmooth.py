def isSmooth(arr):
    l, c = len(arr), len(arr) // 2
    return arr[0] == arr[-1] == arr[c] + (arr[c - 1] * (l % 2 == 0))

