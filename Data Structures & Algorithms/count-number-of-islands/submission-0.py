class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return

            if (r, c) in visited:
                return
            
            visited.add((r, c))

            direc = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for dr, dc in direc:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                
                if (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count

        


