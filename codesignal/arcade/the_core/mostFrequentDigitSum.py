def mostFrequentDigitSum(n):
    ans = []
    while n > 0:
        s = sum(int(i) for i in str(n))
        n = n - s
        ans.append(s)
    
    return max(sorted(ans, reverse=True), key=ans.count)
