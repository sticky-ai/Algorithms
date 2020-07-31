# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    arr = []
    
    while l:
        head = l.value
        arr.append(head)
        l = l.next
    
    for i in range(0, len(arr), k):
        if len(arr) % 3 == 0:
            arr[i:i+k] = arr[i:i+k][::-1]
        else:
            if len(arr) - i < k:
                continue
            else:
                arr[i:i+k] = arr[i:i+k][::-1]
    return arr
