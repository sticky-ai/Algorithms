def replaceMiddle(arr):
    if len(arr) % 2 == 0:
        m = int(len(arr) / 2)
        return arr[:m-1] + [sum(arr[m-1:m+1])] + arr[m+1:]
    return arr
