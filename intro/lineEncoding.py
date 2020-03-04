from itertools import groupby

def lineEncoding(s):
    result = ''
    
    for i, j in groupby(s):
        count = len(list(j))
        if count == 1:
            result += i
        else:
            result += str(count) + i
    return result
