class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = float('-inf')
        prefix = 1
        suffix = 1

        # the core logic to observer the prefix and suffix products
        # 1. All positive
        # 2. even negatives
        # 3. odd negatives
        # 4. zeroes

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n - i - 1]
            max_product = max(max_product, max(prefix, suffix))
        
        return max_product