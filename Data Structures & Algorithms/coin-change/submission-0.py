class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = dict()

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

            
            
        