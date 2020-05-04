def replaceMiddle(arr):
    l, c = len(arr), len(arr) // 2
    sum = arr[c] + (arr[c - 1] * (l % 2 == 0))
    
    if l % 2 == 0:
        return arr[:c-1] + [sum] + arr[c+1:]
    return arr
