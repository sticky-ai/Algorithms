# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def sortZeroOneTwoList(l):
    a = []
    while l:
        a.append(l.value)
        l = l.next
    return sorted(a)
