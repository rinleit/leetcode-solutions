# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        bit = 0
        ans_node = ListNode()
        head_ans = ans_node
        while l1 != None or l2 != None:
            
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + bit
            
            if sum > 9:
                bit = 1
                sum = sum % 10
            else:
                bit = 0

            ans_node.val = sum
            
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
            if l1 or l2: ans_node.next = ListNode()
            if not l1 and not l2:
                if bit: ans_node.next = ListNode(val=1)
            ans_node = ans_node.next

        return head_ans
