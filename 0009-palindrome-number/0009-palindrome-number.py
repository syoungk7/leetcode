class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        return str(x) == str(x)[::-1]
        
        
#         if x == 0 : return True
        
#         tmp_lst = []
#         for char in str(x): 
#             tmp_lst.append(char)

#         tmp = tmp_lst.copy()
#         tmp_lst.reverse()
#         print(tmp_lst, tmp)
#         if tmp_lst == tmp: return True