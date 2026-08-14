class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = dict()
        for ch in s:
            if ch not in char_map:
                char_map[ch] = 0
            char_map[ch] += 1

        for ch in t:
            if ch not in char_map:
                return False
            char_map[ch] -= 1
            if char_map[ch] <= 0:
                del char_map[ch]

        return True
            