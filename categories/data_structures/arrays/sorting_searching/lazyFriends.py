def lazyFriends(houses, maxDist):
    ans = []
    maxRange = [range(h-maxDist, h+maxDist+1) for h in houses]
    for mr in maxRange:
        cnt = 0
        for h in houses:
            if h in mr:
                cnt += 1
        ans.append(cnt - 1)
    return ans
