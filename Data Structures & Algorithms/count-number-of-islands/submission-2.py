class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        def bfs(i, j):
            from collections import deque
            q = deque([(i,j)])
            while q:
                l = len(q)
                for _ in range(l):
                    row, col = q.popleft()
                    if row>=len(grid) or row<0 or col>=len(grid[0]) or col<0 or grid[row][col]=="0":
                        continue
                    else:
                        grid[row][col]="0"
                        q.extend([(row, col+1), (row, col-1), (row+1, col), (row-1, col)])

        length, bridth = len(grid[0]), len(grid)
        for i in range(bridth):
            for j in range(length):
                if grid[i][j]=="1":
                    bfs(i, j)
                    cnt+=1
        return cnt