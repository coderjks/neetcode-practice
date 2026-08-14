class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = dict()
        n = len(nums)
        for i in range(n):
            num_idx_map[nums[i]] = i
        
        for i in range(n):
            diff = target - nums[i]
            if diff in num_idx_map and num_idx_map[diff] != i:
                return [i, num_idx_map[diff]]