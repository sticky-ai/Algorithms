def climbingStairs(n):
    # iter 1 : 1, 0
    # iter 2 : 1, 1
    # iter 3 : 2, 1
    # iter 4 : 3, 2
    # iter 5 : 5, 3
    # iter 6 : 8, 5
    x, y = 1, 0
    for _ in range(n):
        x, y = x + y, x
    return x 


