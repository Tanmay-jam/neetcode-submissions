class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        check=None
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                check = i
        if check==None:
            return False
        s, e = 0, len(matrix[0])
        while s<=e:
            mid = s + (e-s)//2
            if matrix[check][mid]==target:
                return True
            elif matrix[check][mid]<target:
                s=mid+1
            else:
                e=mid-1
        return False
