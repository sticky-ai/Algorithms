def firstReverseTry(arr):
    if len(arr) < 2:
        return arr
    
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

