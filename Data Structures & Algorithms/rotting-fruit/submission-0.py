from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n= len(grid[0])
        queue= deque()
        fresh=0
        minutes=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh +=1
                if grid[i][j]==2:
                    queue.append((i,j))
                # if grid[i][j]==1:
                #     fresh +=1
        direction = [[0,1],[0,-1],[1, 0],[-1, 0]]
                
            # size= len(queue)
        while queue and fresh>0:
            size= len(queue)
            
            for _ in range(size):
                r, c= queue.popleft()
                
                for dr, dc in direction:
                    nr= r + dr
                    nc= c + dc
                    if (nr in range(m) and nc in range(n) and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        queue.append((nr, nc))
                        fresh -=1
            minutes +=1
        return minutes if fresh ==0 else -1                 

        