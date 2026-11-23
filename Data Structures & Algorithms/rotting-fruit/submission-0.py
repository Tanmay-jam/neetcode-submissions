class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j,0))
        
        time=0
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r, c, t = q.popleft()
            time = max(time, t)
            for d in direction:
                nr, nc = r + d[0], c + d[1]
                if 0<=nr and nr<len(grid) and 0<=nc and nc<len(grid[0]):
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc, t+1))
                
        if fresh==0:
            return time
        return -1