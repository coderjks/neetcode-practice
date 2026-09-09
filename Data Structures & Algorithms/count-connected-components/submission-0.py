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
    
    def union(self, x, y) -> None:
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

    
    def isConnected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        du = UnionFind(n)

        for x, y in edges:
            du.union(x, y)

        root_set = set()
        for x in range(n):
            root_set.add(du.find(x))
        
        return len(root_set)
        


