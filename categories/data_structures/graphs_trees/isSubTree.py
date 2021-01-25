#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def check_equal(t1, t2):
    if not t1 and not t2:
        return True
    
    if not t1 or not t2:
        return False
    
    if t1.value != t2.value:
        return False
    
    if not check_equal(t1.left, t2.left):
        return False
        
    if not check_equal(t1.right, t2.right):
        return False
    
    return True
        

def isSubtree(t1, t2):
    if check_equal(t1, t2):
        return True
    
    if t1:
        if isSubtree(t1.left, t2):
            return True
        
        if isSubtree(t1.right, t2):
            return True
        
    return False#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(u, v):
    s = lambda t: ','.join((str(t.value), s(t.left), s(t.right))) if t else '*'
    return not v or s(v) in s(u)
