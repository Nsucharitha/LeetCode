class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        direct = [(0,1),(1,0),(-1,0),(0,-1)]
        dp = [[0] * n for _ in range(m)]


        def dfs(i,j):
            if dp[i][j] !=0:
                return dp[i][j]
            max_len = 1
            for dx, dy in direct:
                x,y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_len = max(max_len, 1+dfs(x,y))
            dp[i][j] = max_len
            return max_len


        result = 0

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i,j))
        return result
                

        