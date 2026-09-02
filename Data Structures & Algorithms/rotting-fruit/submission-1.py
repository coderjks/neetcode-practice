from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh_fruit = 0
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_fruit += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        time_taken = 0
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # standard bfs solution
        while fresh_fruit > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in direc:
                    nr, nc = r + dr, c + dc
                    # skip if out of bounds or already rotten or empty cell
                    if min(nr, nc) < 0 or nr >= n or nc >= m or grid[nr][nc] in (0, 2):
                        continue
                    # mark fruit as rotten
                    grid[nr][nc] = 2
                    # this cell is a fresh fruit and get rotten
                    queue.append((nr, nc))
                    fresh_fruit -= 1
            time_taken += 1
        
        # print(time_taken)
        return -1 if fresh_fruit > 0 else time_taken
