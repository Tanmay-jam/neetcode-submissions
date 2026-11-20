class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def dfs(r, c, it):
            if r>=len(grid) or r<0 or c>=len(grid[0]) or c<0:
                return
            if grid[r][c]=="0":
                return
            grid[r][c]="0"
            nonlocal cnt
            cnt = cnt+1 if it==0 else cnt
            dfs(r+1, c, it+1)
            dfs(r-1, c, it+1)
            dfs(r, c+1, it+1)
            dfs(r, c-1, it+1)


        length, bridth = len(grid[0]), len(grid)
        for i in range(bridth):
            for j in range(length):
                dfs(i, j, 0)
        return cnt