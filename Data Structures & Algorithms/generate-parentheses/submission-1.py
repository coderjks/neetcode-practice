class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(l, r, cur_str):
            if l + r == 2*n:
                ans.append(cur_str)
                return
            
            if l < n:
                helper(l + 1, r, cur_str + "(")
            
            # check if 
            if l > r:
                helper(l, r + 1, cur_str + ")")

        helper(0, 0, "")
        return ans
        
        