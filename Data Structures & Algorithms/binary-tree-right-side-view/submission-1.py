# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])

        while queue:
            size = len(queue)
            rightSide = None

            while size > 0:
                node = queue.popleft()
                if node:
                    rightSide = node.val
                    queue.append(node.left)
                    queue.append(node.right)
                size -= 1
            
            if rightSide:
                ans.append(rightSide)

        return ans