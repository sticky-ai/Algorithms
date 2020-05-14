def arrayPreviousLess(items):
    ans = [-1]
    for i in range(1, len(items)):
        if items[i] <= min(items[i::-1]):
            ans.append(-1)
            continue
        for j in items[i::-1]:
            if items[i] > j:
                ans.append(j)
                break
    return ans
