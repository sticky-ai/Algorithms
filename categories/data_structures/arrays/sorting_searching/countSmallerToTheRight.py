def countSmallerToTheRight(nums):
    ans = 0
    for i in range(len(nums) - 1):
        c = 0
        for j in nums[i+1:]:
            if nums[i] > j:
                c += 1
        ans += c
    return ans
