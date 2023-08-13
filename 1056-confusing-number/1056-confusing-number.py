class Solution:
    def confusingNumber(self, n: int) -> bool:
        new_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        new = ""
        
        for i in str(n):
            i = int(i)
            if i not in new_map: return False
            print(new_map[i])
            new += str(new_map[i])

        if int(n) != int(new[::-1]): return True
        
        return False
            

#         for num in str(n):
#             if num in '23457': return False
#             if num in '96':
#                 if num == '9': num = '6' 
#                 else: num = '9' 
#             new.append(num)
#         if int(n) != int(''.join(new[::-1])): return True
#         return False
    
#     class Solution:
#     def confusingNumber(self, n: int) -> bool:
#         digit_rotation_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
#         num_str = str(n)
#         new_num_str = ""
#         for digit in num_str[::-1]:
#             if int(digit) not in digit_rotation_map:
#                 return False
            
#             new_num_str += str(digit_rotation_map[int(digit)])

#         if n == int(new_num_str):
#             return False
#         return True