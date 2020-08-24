def composeRanges(nums):
    if not nums: 
        return []
    
    start, end, res = nums[0], nums[0], []
    for n in nums[1:]:
        if n - end != 1:
            res.append(f'{start}->{end}' if start != end else str(start))
            start = n
        end = n
    res.append(f'{start}->{end}' if start != end else str(start))
    return res
    
