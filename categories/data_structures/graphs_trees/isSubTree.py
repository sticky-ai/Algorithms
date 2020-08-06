#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(u, v):
    s = lambda t: ','.join((str(t.value), s(t.left), s(t.right))) if t else '*'
    return not v or s(v) in s(u)
