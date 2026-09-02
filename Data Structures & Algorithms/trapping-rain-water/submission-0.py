class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        res = 0

        while left <= right:
            if height[left] <= height[right]:
                leftMax = max(leftMax, height[left])
                res += max(leftMax - height[left], 0)
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                res += max(rightMax - height[right], 0)
                right -= 1
        
        return res
