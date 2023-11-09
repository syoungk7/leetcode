class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        ocean_view = []
        count = len(heights) -1
        
        while count != -1:
            if highest < heights[count]:
                ocean_view.append(count)
            highest = max(highest, heights[count])
            count -= 1
        return ocean_view[::-1]