class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited_col = set()
        anti_diag = set()
        diag = set()
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def backtrack(r, board):
            if r == n:
                ans.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in visited_col or (c - r) in diag or (r + c) in anti_diag:
                    continue

                board[r][c] = "Q"
                visited_col.add(c)
                anti_diag.add(r + c)
                diag.add(c - r)

                backtrack(r + 1, board)

                board[r][c] = "."
                visited_col.remove(c)
                anti_diag.remove(r + c)
                diag.remove(c - r)
        
        backtrack(0, board)
        return ans
