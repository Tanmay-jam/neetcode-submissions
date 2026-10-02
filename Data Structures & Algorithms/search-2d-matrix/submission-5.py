class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        s, e = 0, rows*cols -1
        while s<=e:
            mid = s + (e-s)//2
            r = mid//cols
            c = mid%cols
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                s=mid+1
            else:
                e=mid-1
        return False
