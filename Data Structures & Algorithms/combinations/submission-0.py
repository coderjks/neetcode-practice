class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i, curComb):
            if len(curComb) == k:
                ans.append(curComb.copy())
                return
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                backtrack(j + 1, curComb + [j])
        
        backtrack(1, [])
        return ans