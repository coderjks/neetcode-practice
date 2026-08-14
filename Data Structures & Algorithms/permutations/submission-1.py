class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nextPerms = [[]]

        for n in nums:
            resPerm = []
            for p in nextPerms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, n)
                    resPerm.append(pCopy)
            nextPerms = resPerm
        
        return nextPerms


        # def helper(i, nums):
        #     if i == len(nums):
        #         return [[]]
            
        #     nextPerms = []
        #     perms = helper(i + 1, nums)

        #     for p in perms:
        #         for j in range(len(p) + 1):
        #             pCopy = p.copy()
        #             pCopy.insert(j, nums[i])
        #             nextPerms.append(pCopy)
            
        #     return nextPerms
        
        # return helper(0, nums)
                
