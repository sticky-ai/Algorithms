
from bisect import bisect_left, bisect_right
def lazyFriends(houses, maxDist):
    return [bisect_right(houses, houses[i]+maxDist) - bisect_left(houses, houses[i]-maxDist)-1 for i in range(len(houses))]
