class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                row = i
                break
        if row is None:
            return False
        s, e = 0, len(matrix[row])-1
        while s<=e:
            mid = s + (e-s)//2
            if target==matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                e = mid-1
            else:
                s = mid+1
        return False