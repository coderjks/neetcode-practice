class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dict()
        ans = [0]

        # print(char_map)
        def helper(i, s):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i in dp:
                return dp[i]

            # choose i as valid
            res = helper(i + 1, s)

            # choose next 2 char group if valid
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'):
                    res += helper(i + 2, s)
            
            dp[i] = res
            return res
        
        return helper(0, s)


            
        