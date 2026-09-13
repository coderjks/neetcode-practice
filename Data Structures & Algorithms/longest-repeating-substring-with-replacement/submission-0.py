class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window is invalid -> cur_window - maxf > k:
        char_freq = {}
        maxf = 0
        l = 0
        res = 0

        for r in range(len(s)):
            ch = s[r]
            char_freq[ch] = 1 + char_freq.get(ch, 0)
            maxf = max(maxf, char_freq[ch])
            while (r - l + 1) - maxf > k:
                char_freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
