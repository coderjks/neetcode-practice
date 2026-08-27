class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if (total % 2) != 0:
            return False
        
        target = total // 2
        n = len(nums)
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        
        # sum is even can partition
        def helper(i, target):
            if target == 0:
                return True
            
            if i >= n or target < 0:
                return False
            
            if dp[i][target] != -1:
                return dp[i][target]
            
            dp[i][target] = (helper(i + 1, target - nums[i]) or helper(i + 1, target))
            return dp[i][target]
        
        return helper(0, target)
            