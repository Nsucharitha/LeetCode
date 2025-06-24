class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        #to track used columns, and diagonals
        visited_col = set()
        visited_diag = set()  #r-c
        visited_antidiag = set() #r+c

        def backtrack(r):
            if r==n:
                #convert board rows to strings and store a deep copy
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                #diagonals
                diag = r-c
                anti_diag = r+c

                #see if placing a queen at (r,c) is safe
                if c in visited_col or diag in visited_diag or anti_diag in visited_antidiag:
                    continue

                #put queen
                visited_col.add(c)
                visited_diag.add(diag)
                visited_antidiag.add(anti_diag)
                board[r][c] = "Q"

                #recurse
                backtrack(r+1)   

                #backtrack
                board[r][c] = "."
                visited_col.remove(c)
                visited_diag.remove(diag)
                visited_antidiag.remove(anti_diag)


        backtrack(0)
        return res     