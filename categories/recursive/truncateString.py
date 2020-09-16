def truncateString(s):
    arr = list(map(int, list(s)))
    if arr == []: return ''
    
    if len(arr) > 1 and (arr[0] + arr[-1]) % 3 == 0:
        del arr[0], arr[-1]
    
    elif arr[-1] % 3 == 0:
        del arr[-1]
    
    elif arr[0] % 3 == 0:
        del arr[0]
    
    if arr == s:
        return ''.join(map(str, arr))
    else:
        return truncateString(arr)
    
