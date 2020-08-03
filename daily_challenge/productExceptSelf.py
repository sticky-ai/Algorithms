n, m = eval(dir()[0])
s = 0
p = 1
for n in N:
    s, p = (s * n + p) % m, p * n % m
return s

# def productExceptSelf(nums, m):
#     s = 0
#     p = 1
#     for n in nums:
#         s, p = (s * n + p) % m, p * n % m
#     return s
