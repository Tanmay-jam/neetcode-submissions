class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        temp=intervals[0]
        cnt=0
        for i in range(1, len(intervals)):
            if temp[1]>intervals[i][0] and temp[0]<intervals[i][1]:
                temp[1] = min(temp[1], intervals[i][1])
                cnt+=1
            else:
                temp = intervals[i]
        return cnt