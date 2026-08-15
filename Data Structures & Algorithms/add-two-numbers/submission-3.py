# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = curNode = ListNode()
        carry = 0

        while l1 or l2 or carry:
            x = y = 0
            if l1:
                x = l1.val
                l1 = l1.next

            if l2:
                y = l2.val 
                l2 = l2.next

            cur_sum = x + y + carry
            carry = cur_sum // 10
            curNode.next = ListNode(cur_sum % 10)
            curNode = curNode.next
        
        return dummyNode.next

        
