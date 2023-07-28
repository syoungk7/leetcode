class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        
        s1, s2 = 0, 0
        
        while s1 < len(slots1) and s2 < len(slots2):
            i, j = slots1[s1], slots2[s2]
            
            if min(i[1], j[1]) - max(i[0], j[0]) >= duration:
                return [max(i[0], j[0]), max(i[0], j[0]) + duration]       

            if j[1] < i[1]:
                s2 += 1
            else:
                s1 += 1

## Time Limit Exceeded        
#         for i in sorted(slots2):
#             for j in sorted(slots1):
#                 if min(i[1], j[1]) - max(i[0], j[0]) >= duration:
#                     return [max(i[0], j[0]), max(i[0], j[0]) + duration]
                
#                 if j[1] < i[1]:
#                     continue
#                 elif j[1] > i[1]:
#                     break
                    
        return []
                