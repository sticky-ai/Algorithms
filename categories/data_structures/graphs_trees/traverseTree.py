#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

from collections import deque

def traverseTree(t):    
    if not t: return []
    visited = []
    queue = deque([t])
    
    while queue:
        node = queue.popleft()
        visited.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited
