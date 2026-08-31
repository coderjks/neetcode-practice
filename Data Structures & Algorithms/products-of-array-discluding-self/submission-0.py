class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            prod[i] = prod[i + 1] * nums[i]
        
        cur_prod = 1

        for i in range(n):
            num = nums[i]
            nums[i] = prod[i + 1] * cur_prod
            cur_prod *= num
        
        return nums


        