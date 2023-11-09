class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        ocean_view = []
        count = len(heights) -1
        
        while count != -1:
            #print(count, highest, heights[count])
            if highest < heights[count]:
                ocean_view.append(count)
                highest = heights[count]
            count -= 1
        #print(ocean_view)
        return ocean_view[::-1]