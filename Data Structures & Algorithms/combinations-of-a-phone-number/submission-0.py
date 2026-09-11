class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)
        digit_char_map  = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, n, size, cur_str):
            if size > 0 and size == n:
                ans.append(cur_str)
                return

            for j in range(i, n):
                for ch in digit_char_map[digits[j]]:
                    dfs(j + 1, n, size + 1, cur_str + ch)
        
        dfs(0, n, 0, '')
        return ans

