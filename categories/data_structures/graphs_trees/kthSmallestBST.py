#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def kthSmallestInBST(t, k):
    def dfs(n):
        if n:
            yield from dfs(n.left)
            yield n.value
            yield from dfs(n.right)
    
    f = dfs(t)
    
    for _ in range(k):
        ans = next(f)
    return ans
