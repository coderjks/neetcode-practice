# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = curNode = ListNode()
        heap = list()

        for listNode in lists:
            if not listNode:
                continue
            heapq.heappush(heap, listNode)
        
        while heap:
            # get min node from heap
            listNode = heapq.heappop(heap)

            curNode.next = listNode
            curNode = curNode.next
            
            # push the next node in heap
            if listNode.next:
                listNode = listNode.next
                heapq.heappush(heap, listNode)
        
        return dummyNode.next

        
            
            
        