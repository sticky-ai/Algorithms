def composeRanges(nums):
    if not nums: 
        return []
    s, e, r = nums[0], nums[0], []
    for x in nums[1:]:
        if x - e != 1:
            r.append(f'{s}->{e}' if s != e else str(s))
            s = x
        e = x
    r.append(f'{s}->{e}' if s != e else str(s))
    return r

