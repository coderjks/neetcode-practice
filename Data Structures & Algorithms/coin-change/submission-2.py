class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else - 1


        n = len(coins)
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(n + 1)]

        # amount is 0, coins required will be 0 for any number of coins we have
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                coin = coins[i - 1]
                if j >= coin:
                    dp[i][j] = 1 + dp[i][j - coin]
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
        
        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]

        # below is a recursive solution
        def helper(i, target):
            if target == 0:
                return 0
            
            if (i, target) in dp:
                return dp[(i, target)]
            
            if i >= len(coins) or target < 0:
                return float('inf')
            
            res = min(1 + helper(i, target - coins[i]), helper(i + 1, target))
            dp[(i, target)] = res
            return res

        ans = helper(0, amount)
        return -1 if ans == float('inf') else ans

            
            
        