class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        k = 0
        while j < n:
            if j != 0 and nums[j] != nums[j - 1]:
                i += 1
                nums[i] = nums[j]
                k += 1
            
            while j < n - 1 and nums[j] == nums[j + 1]:
                # continuosly skip the repeated numbers
                j += 1

            j += 1
        
        return k + 1
        

