#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isTreeSymmetric(t):
    if not t:
        return True
    
    stack = [(t.left, t.right)] 
    while stack:
        left, right = stack.pop()
        if left and right and left.value == right.value:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
            continue
        
        if not left and not right:
            continue
        
        return False

    return True
