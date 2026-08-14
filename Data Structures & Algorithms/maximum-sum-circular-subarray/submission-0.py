class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = curMin = 0
        globMax = globMin = nums[0]

        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
            total += n
        
        return max(globMax, total - globMin) if globMax > 0 else globMax
