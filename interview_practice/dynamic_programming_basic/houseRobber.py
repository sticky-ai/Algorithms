def houseRobber(nums):
    x = y = 0
    for n in nums:
        x, y = y + n, max(x, y)
    return max(x, y)

