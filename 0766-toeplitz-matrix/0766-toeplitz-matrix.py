class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        # 
        for i in range(len(matrix)-1):
            if matrix[i][0:len(matrix[i])-1] != matrix[i+1][1::]:
                return False
        else:
            return True
            
            
            
#         de = deque(matrix[0])
        
#         for i in range(len(matrix)-1):
#             de.pop()
    
#             if list(de) == matrix[i+1][1::]:
#                 de.extendleft([matrix[i+1][0]])
#             else: 
#                 return False
            
#         return True


        
        