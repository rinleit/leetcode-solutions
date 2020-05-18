# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from bisect import insort
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        numbers = []
        for list_node in lists:
            head = list_node
            while head != None:
                insort(numbers, head.val)
                head = head.next
        if not numbers: return None
        node = ListNode(-1)
        head = node
        for n in numbers:
            node.next = ListNode()
            node = node.next
            node.val = n
        return head.next
