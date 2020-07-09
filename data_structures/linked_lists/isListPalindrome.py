# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def isListPalindrome(l):
    m = []
    while l:
        m.append(l.value) 
        l = l.next
    return m == m[::-1]
