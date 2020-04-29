# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    m = []
    while l:
        head = l.value
        if (head != k):
            m.append(head)      
        l = l.next
    return m
