from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        LAND_CELL = 2147483647
        DIREC = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            queue = deque([(0, r, c)])

            while queue:
                # d is distance
                d, r, c = queue.popleft()

                for dr, dc in DIREC:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C:
                        continue

                    if d + 1 < grid[nr][nc]:
                        grid[nr][nc] = d + 1
                        queue.append((d + 1, nr, nc))
        
        # start bfs from all treasure cell
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    bfs(i, j)
        

                


