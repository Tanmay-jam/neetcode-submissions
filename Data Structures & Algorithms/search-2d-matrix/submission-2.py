class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e  = 0, len(matrix)*len(matrix[0])-1

        while s<=e:
            mid = s + (e-s)//2
            row = mid//len(matrix[0])
            col = mid%len(matrix[0])

            if target==matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                e = mid-1
            else:
                s = mid + 1
        return False