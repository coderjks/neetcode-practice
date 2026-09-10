class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]
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
    
    def isConnected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        ans = None

        for u, v in edges:
            if not uf.union(u - 1, v - 1):
                ans = [u, v]
        return ans
