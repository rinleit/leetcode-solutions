from bisect import insort
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        sortlist = []
        while head != None:
            insort(sortlist, head.val)
            head = head.next
        if not sortlist: return None
        node = ListNode()
        pnode = node
        for idx, val in enumerate(sortlist):
            node.val = val
            if idx < len(sortlist) - 1:
                node.next = ListNode()
            node = node.next
        return pnode