class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and word == s[i:i+len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        
        return dp[0]
        
        def dp(i):
            if i == 0:
                return True

            for word in wordDict:
                n = len(word)
                if i < n or word != s[i - n: i]:
                    continue
                if dp(i - n):
                    return True
            return False
        
        return dp(len(s))
                
                