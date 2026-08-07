class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix)*len(matrix[0])-1
        while s<=e:
            mid = (e-s)//2 + s
            row = mid//len(matrix[0])
            col = mid%len(matrix[0])

            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                s=mid+1
            else:
                e=mid-1
        return False