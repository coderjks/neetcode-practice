class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j -= 1
            else:
                i += 1
        
        return -1

