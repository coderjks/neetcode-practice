class Solution:
    def numDecodings(self, s: str) -> int:
        # this entry is for the base case
        n = len(s)
        dp = {n: 1}

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] += dp[i + 2]
        
        return dp[0]

        # print(char_map)
        def helper(i, s):
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0
            
            # choose i as valid
            res = helper(i + 1, s)

            # choose next 2 char group if valid
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'):
                    res += helper(i + 2, s)
            
            dp[i] = res
            return res
        
        return helper(0, s)


            
        