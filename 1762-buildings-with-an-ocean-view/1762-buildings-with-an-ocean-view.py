class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        ocean_view = deque()
        count = len(heights) -1
        
        while count != -1:
            if highest < heights[count]:
                ocean_view.appendleft(count)
                highest = heights[count]
            #highest = max(highest, heights[count])
            count -= 1
        return ocean_view
