class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n - 1

        while l <= h:
            m = (l + h) // 2
            if target == nums[m]:
                return m
            elif nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    h = m - 1
            else:
                if target < nums[m] or target > nums[h]:
                    h = m - 1
                else:
                    l = m + 1
        
        return -1
