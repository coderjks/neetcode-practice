# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseKNodes(node, k):
                    prev = None
                    cur = node
                    count = 0
                    while count < k and cur:
                        next_node = cur.next
                        cur.next = prev
                        prev = cur
                        cur = next_node
                        count += 1
            
                    if count < k:
                        return reverseKNodes(prev, count)
                    
                    # node is the tail now
                    return prev, node, cur

        def helper(node):
            if not node:
                return
            newHead, newTail, nextHead = reverseKNodes(node, k)
            newTail.next = helper(nextHead)
            return newHead
        
        return helper(head)
        



        