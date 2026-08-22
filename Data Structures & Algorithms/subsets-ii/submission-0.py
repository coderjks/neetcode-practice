class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums = sorted(nums)

        def backtrack(idx, cur_set):
            ans.append(cur_set.copy())
            
            for i in range(idx, n):
                if i != idx and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, cur_set + [nums[i]])

        backtrack(0, [])
        return list(ans)
                

