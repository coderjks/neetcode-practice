# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = curNode = ListNode()
        heap = list()

        for idx, listNode in enumerate(lists):
            if not listNode:
                continue
            heapq.heappush(heap, (listNode.val, idx, listNode))
        
        while heap:
            # get min node from heap
            val, idx, listNode = heapq.heappop(heap)

            curNode.next = listNode
            curNode = curNode.next
            
            # push the next node in heap
            if listNode.next:
                listNode = listNode.next
                heapq.heappush(heap, (listNode.val, idx, listNode))
        
        return dummyNode.next

        
            
            
        