# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        firstPtr = head
        secondPtr  = dummy

        while n > 0:
            firstPtr = firstPtr.next
            n -= 1

        while firstPtr:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        secondPtr.next = secondPtr.next.next

        return dummy.next
        

            