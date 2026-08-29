class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        while num_set:
            num = max(num_set)
            cur_len = 0
            while num in num_set:
                cur_len += 1
                num_set.remove(num)
                num -= 1
            max_len = max(max_len, cur_len)

        return max_len


