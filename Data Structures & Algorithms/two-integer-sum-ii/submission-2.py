class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i<j:
            twosum = numbers[i] + numbers[j]
            if twosum==target:
                return [i+1, j+1]
            elif twosum<target:
                i+=1
            else:
                j-=1