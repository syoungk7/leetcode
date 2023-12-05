class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        de = deque(matrix[0])
        print(deque)
        
        for i in range(len(matrix)-1):
            de.pop()
    
            if list(de) == matrix[i+1][1::]:
                de.extendleft([matrix[i+1][0]])

            else: return False
            
        return True