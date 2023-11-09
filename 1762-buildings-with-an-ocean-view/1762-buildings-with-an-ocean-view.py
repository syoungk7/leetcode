class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
#         highest = 0
#         ocean_view = []
#         count = len(heights) -1
        
#         while count != -1:
#             if highest < heights[count]:
#                 ocean_view.append(count)
#                 highest = heights[count]
#             #highest = max(highest, heights[count])
#             count -= 1
#         return ocean_view[::-1]
    
        max_height_from_right = 0
        res = deque()

        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_height_from_right:
                res.appendleft(i)
            max_height_from_right = max(max_height_from_right, heights[i])

        return res