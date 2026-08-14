class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = list()
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                # c is closing bracket
                if stack and stack[-1] == brackets_map[c]:
                     stack.pop()
                else: 
                    return False
        return False if stack else True