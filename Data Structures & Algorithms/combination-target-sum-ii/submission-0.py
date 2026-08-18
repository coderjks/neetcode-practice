class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []

        def backtrack(i, n, cur_comb, target):
            if target == 0:
                ans.append(cur_comb.copy())
                return
            
            for j in range(i, n):
                if i != j and candidates[j] == candidates[j - 1]:
                    continue
                
                candidate = candidates[j]
                if target >= candidate:
                    backtrack(j + 1, n, cur_comb + [candidate], target - candidate)
        
        backtrack(0, len(candidates), [], target)
        return ans
                
                

