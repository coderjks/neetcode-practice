class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0

        while j < n:
            nums[i] = nums[j]
            while j < n and nums[j] == nums[i]:
                j += 1
            i += 1
        return i
