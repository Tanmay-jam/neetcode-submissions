class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = intervals[0]
        res = []
        for i in range(1,len(intervals)):
            if temp[1]>=intervals[i][0] and temp[0]<=intervals[i][1]:
                temp[0] = min(temp[0], intervals[i][0])
                temp[1] = max(temp[1], intervals[i][1])
            else:
                res.append(temp)
                temp = intervals[i]
        res.append(temp)
        return res