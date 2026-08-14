class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
    
        def backtrack(i, n, target, cur_sum, cur_set):
            if target == cur_sum:
                ans.append(cur_set.copy())
                return
            
            for i in range(i, n):
                num = nums[i]
                if target - (cur_sum + num) >= 0:
                    cur_set.append(num)
                    backtrack(i, n, target, cur_sum + num, cur_set)
                    cur_set.pop()
        
        backtrack(0, len(nums), target, 0, [])
        return ans