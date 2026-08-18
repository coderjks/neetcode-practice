class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            odd_substr = self.helper(i, i, s)
            if len(odd_substr) > len(ans):
                ans = odd_substr
        
        for i in range(len(s) - 1):
            even_substr = self.helper(i, i + 1, s)
            if len(even_substr) > len(ans):
                ans = even_substr
        
        return ans


    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        
        return s[l + 1: r]
        
       


