# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow now points to mid of the list, hence next node marks start of the second half
        l2 = slow.next
        slow.next = None

        # now head is l1, l2 is other half reversed
        l1 = head
        l2 = self.reverseList(l2)
        
        l3 = dummy = ListNode()

        while l1 or l2:
            if l1:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next

            if l2:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        
        # return l3.next


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        cur_ptr = head

        while cur_ptr:
            next_ptr = cur_ptr.next
            cur_ptr.next = prev
            prev = cur_ptr
            cur_ptr = next_ptr
        
        return prev

    
