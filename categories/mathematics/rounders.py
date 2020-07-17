def rounders(n):
    nums = list(map(int, (str(n))))
    for i in range(len(nums)-1, 0, -1):
        if nums[i] != 0:
            if nums[i] >= 5:
                nums[i] = 0
                nums[i-1] += 1
            if nums[i] < 5:
                nums[i] = 0
    return int(''.join(map(str, nums)))
    
