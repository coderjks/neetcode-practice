# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head
            
        secondPtr = firstPtr = head

        for _ in range(n):
            firstPtr = firstPtr.next

        while firstPtr and firstPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        if not firstPtr:
            return head.next
        
        secondPtr.next = secondPtr.next.next

        return head
        

            