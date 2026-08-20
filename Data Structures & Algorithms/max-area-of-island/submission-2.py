class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if grid[r][c] == 0:
                return 0
            
            # mark this cell as visited
            grid[r][c] = 0

            direc = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            cur_area = 1

            for dr, dc in direc:
                nr, nc = r + dr, c + dc
                cur_area += dfs(nr, nc)
            
            return cur_area
            

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
        