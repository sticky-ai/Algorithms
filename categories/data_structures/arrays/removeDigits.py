def removeDigits(n, k):
    res = [int(str(n)[i:k+i]) for i in range(len(str(n))) if len(str(n)[i:k+i]) == k]
    return [min(res), max(res)]
