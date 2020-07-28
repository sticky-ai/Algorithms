# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    arr = []
    while l:
        h = l.value
        arr.append(h)
        l = l.next
    
    arr.append(value)
    return sorted(arr)
