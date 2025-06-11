
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Create a (ROWS+1) x (COLS+1) grid filled with infinity
        res = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Set the cell just outside the bottom-right corner to 0
        res[ROWS - 1][COLS] = 0

        # Iterate from bottom-right to top-left
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        
        # Final result at top-left
        return res[0][0]
