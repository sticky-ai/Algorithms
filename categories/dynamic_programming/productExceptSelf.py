"""
You have an array nums. We determine two functions to perform on nums. In both cases, n is the length of nums:

fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. (In other words, fi(nums) is the product of all array elements except the ithf.)
g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).
Using these two functions, calculate all values of f modulo the given m. Take these new values and add them together to get g. You should return the value of g modulo the given m.
"""

from functools import reduce

def productExceptSelf(nums, m):
    s = 0
    p = 1
    for n in nums:
        s, p = (s * n + p) % m, p * n % m
        print(s, p)
    return s
        
    # res = 0
    # f = lambda x, y: x * y
    # for n in nums:
    #     temp = nums.copy()
    #     temp.remove(n)
    #     res += reduce(f, temp) % m
    # return res % m
    
    # res = []
    # for i in range(len(nums)):
    #     temp = [nums[j] for j in range(len(nums)) if i != j]
    #     res.append(reduce(lambda x, y: x * y, temp))
    # return sum(res) % m
