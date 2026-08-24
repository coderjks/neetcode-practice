from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        queue = deque()
        Direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        dist = 0

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                for dr, dc in Direc:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= R or nc >= C or (nr, nc) in visited or grid[nr][nc] == -1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))

            dist += 1      


