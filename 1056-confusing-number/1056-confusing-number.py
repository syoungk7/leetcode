class Solution:
    def confusingNumber(self, n: int) -> bool:
        new_map = {'6': '9', '9': '6'}
        new = ""
        
        for i in str(n):
            if i in '23457': return False
            if i == '9' or i == '6': new += new_map[i]
            else: new += i


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
