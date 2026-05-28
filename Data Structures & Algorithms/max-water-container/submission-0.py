class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = -1
        distance = len(heights)-1
        l, r = 0, distance
        while l<r:
            water = 0
            if heights[l] > heights[r]:
                water = heights[r]*distance
                r-=1
            else:
                water = heights[l]*distance
                l+=1
            distance -= 1
            if water > maxWater:
                maxWater = water
        return maxWater
