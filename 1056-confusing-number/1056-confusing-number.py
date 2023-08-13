class Solution:
    def confusingNumber(self, n: int) -> bool:
        new_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        new = ""
        
        for i in str(n):
            if i not in new_map: return False
            new += new_map[i]

        if int(n) != int(new[::-1]): return True
        
        return False
            
#         num = []
#         for num in str(n):
#             if num in '23457': return False
#             if num in '96':
#                 if num == '9': num = '6' 
#                 else: num = '9' 
#             new.append(num)
#         if int(n) != int(''.join(new[::-1])): return True
#         return False
