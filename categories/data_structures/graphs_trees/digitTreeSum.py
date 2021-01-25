#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def digitTreeSum(t):
    if not t:
        return 0
    
    stack = [(t, 0)]
    s = 0
    
    while stack:
        cur, v = stack.pop()
        
        if cur.left or cur.right:    
            if cur.left:
                stack.append((cur.left, cur.value + v * 10))
            if cur.right:
                stack.append((cur.right, cur.value + v * 10))
        else:
            s += cur.value + v * 10
    
    return s
