def equilibriumPoint(arr):
    s = sum(arr)
    for i in range(len(arr)):
        t = sum(arr[:i]) 
        if t == (s - t - arr[i]):
            return i + 1
    return -1
