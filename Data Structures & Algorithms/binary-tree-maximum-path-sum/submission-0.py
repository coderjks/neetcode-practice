# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-1001]


        def helper(root):
            if not root:
                return -1001
            
            l = helper(root.left)
            r = helper(root.right)
            
            ans[0] = max(ans[0], max(root.val, root.val + l + r))
            ans[0] = max(ans[0], max(root.val + l, root.val + r))

            return max(root.val, root.val + l, root.val + r)

        helper(root)
        return ans[0]

            

        