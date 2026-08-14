class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = list()
# (())[] - True. []
# ()()[ - False. [
# (())] - False. ]
#  ()()((()))[)
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                # c is closing bracket
                if not stack:
                    return False
                if stack[-1] != brackets_map[c]:
                    return False
                stack.pop()
        
        return False if stack else True