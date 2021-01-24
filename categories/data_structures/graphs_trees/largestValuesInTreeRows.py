#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import deque

def largestValuesInTreeRows(t):
    if not t: return []
    
    ans = []
    queue = deque([t])
    while queue:
        mx = float('-inf')
        temp = []
        for v in queue:
            if not v: continue
            mx = max(mx, v.value)
            
            if v.left:
                temp.append(v.left)
            if v.right:
                temp.append(v.right)
        queue = temp
        ans.append(mx)
    return ans
