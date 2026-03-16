from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Each iteration is counted as minute. 
        # At each iteration bfs 1 level and then see if they can be rotten.  
        # Termination is when no rotten oranges in queue are there or all oranegs are rotten. 
        def canBecomeRotten(r,c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == 1

        queue = deque() # Only add rotten ones to the queue. 

        total_clean = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    total_clean += 1
        res = 0
        while queue and total_clean > 0:
            for _ in range(len(queue)):
                (r,c) = queue.popleft()
                # Check and add adjacent elemtns to queue if they become rotten.
                for i,j in [(0, 1), (1,0), (0, -1), (-1, 0)]:
                    if canBecomeRotten(r+i, c+j):
                        grid[r+i][c+j] = 2
                        total_clean -= 1
                        queue.append((r+i,c+j))
            res += 1
        
        if total_clean == 0:
            return res
        return -1








        