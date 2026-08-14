# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is middle
        head2 = slow.next
        slow.next = None
        head2 = self.reverse(head2)

        res = 0
        while head and head2:
            res = max(res, head.val + head2.val)
        
            head = head.next
            head2 = head2.next
        
        return res


    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev
        