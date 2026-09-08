# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]


        def helper(root):
            if not root:
                return -1001
            
            l = helper(root.left)
            r = helper(root.right)
            l = max(l, 0)
            r = max(r, 0)
            
            ans[0] = max(ans[0], root.val + l + r)

            return root.val + max(l, r)

        helper(root)
        return ans[0]

            

        