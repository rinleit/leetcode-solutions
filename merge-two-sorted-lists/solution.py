from bisect import insort
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergelst = []
        while l1 != None or l2 != None:
            if l1:
                insort(mergelst, l1.val)
                l1 = l1.next
            if l2:
                insort(mergelst, l2.val)
                l2 = l2.next
        node = ListNode()
        head = node
        n = len(mergelst)
        for i in range(n):
            node.val = mergelst[i]
            if i < n - 1: node.next = ListNode()
            node = node.next
        return head if n else None