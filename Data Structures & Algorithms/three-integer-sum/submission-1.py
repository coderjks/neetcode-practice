class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        ans = []

        while i < n:
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            
            target = -nums[i]

            # two sum here
            left, right = i + 1, n - 1
            # need atleast 2 elements 
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1

            # increment
            i += 1
        return ans
