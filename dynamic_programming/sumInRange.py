def sumInRange(nums, queries):

    def prefix_sum(nums):
        accu = 0
        yield accu
               
        for n in nums:
            accu += n
            yield accu

    nums = list(prefix_sum(nums))
    return sum([nums[r + 1] - nums[l] for l, r in queries]) % (1000000007)
    
    #print(nums)
#    n = [sum(nums[l:r+1]) for l, r in queries]
#    return sum(n) % 1000000007

