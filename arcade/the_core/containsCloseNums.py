def containsCloseNums(nums, k):
    d = {}
    for idx, num in enumerate(nums):
        if num in d and idx - d[num] <= k:
            return True
        d[num] = idx
    return False
