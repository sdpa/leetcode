class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # For each cell in the grid perfrom a dfs search. End DFS if you reach the end or reach a 0
        # The number of islands is the number of times you perfrom dfs.
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            
            # Top, Right, Botton, Left.
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            
            

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1

        return count
        


        