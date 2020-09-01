def longestSequence(a):
    cnt = 1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            diff = a[j] - a[i]
            if diff == 0:
                continue
            tmp = 1
            mx = a[i]
            for k in range(j, len(a)):
                if a[k] - mx == diff:
                    tmp += 1
                    mx = a[k]
            if tmp > cnt:
                cnt = tmp
    return cnt
