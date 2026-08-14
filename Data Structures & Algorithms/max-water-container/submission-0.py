class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        max_water = float('-inf')

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            max_water = max(water, max_water)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l, r = l + 1, r - 1
        
        return max_water

        