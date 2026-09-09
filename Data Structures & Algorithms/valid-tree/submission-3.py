class DSU:

    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1 for i in range(n)] # keep the tree balance
    
    def find(self, x) -> int:
        if x == self.root[x]:
            return x
        # path compression technique
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        du = DSU(n)
        res = n

        for u, v in edges:
            # These are already connected 
            if not du.union(u, v):
                return False
            res -= 1
        
        return res == 1

                

        