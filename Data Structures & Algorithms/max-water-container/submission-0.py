class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, h = 0, len(heights)-1
        while l<h:
            area = (h-l)*min(heights[h], heights[l])
            if area>maxA:
                maxA=area
            if heights[h] == min(heights[h], heights[l]):
                h-=1
            else:
                l+=1
        return maxA