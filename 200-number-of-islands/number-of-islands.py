class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c,matrix):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
                return
            if matrix[r][c] == '0':
                return
            if matrix[r][c] == '1':
                matrix[r][c] = -1
                dfs(r-1, c, matrix)
                dfs(r, c+1, matrix)
                dfs(r+1, c, matrix)
                dfs(r, c-1, matrix)


        num = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r,c,grid)
                    num += 1
        return num

        
        