class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        l = r = 0

        while r < len(nums):
            if nums[r] in num_set:
                return True
            num_set.add(nums[r])

            if r - l + 1 > k:
                num_set.remove(nums[l])
                l += 1
            r += 1
        
        return False