class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        l = 0

        for r in range(len(nums)):
            # this means you will never add a -ve cur_sum to current number
            # hence reset to 0 and move l to r
            if cur_sum < 0:
                cur_sum = 0
                l = r
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum