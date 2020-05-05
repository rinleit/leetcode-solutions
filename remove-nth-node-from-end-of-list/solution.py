# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        hhead = head
        i = 1
        while head.next != None:
            head = head.next
            i += 1
        phead = hhead
        k = i-n
        while k > 1:
            phead = phead.next
            k -= 1 
        if phead.next != None and k != 0:
            phead.next = phead.next.next
        else:
            return hhead.next
        return hhead
