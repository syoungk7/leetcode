class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # #tmp = ''.join([char for char in s if char.isalpha() or char.isnumeric()]).lower()
        # tmp = ''.join([char for char in s if char.isalnum()]).lower()
        # # print(tmp)
        # return tmp == tmp[::-1]

        ## two points
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum(): left += 1
            while left < right and not s[right].isalnum(): right -= 1
            if s[left].lower() != s[right].lower(): return False

            left += 1
            right -= 1
        return True   

#         regex = re.compile('[^a-zA-Z0-9]')

#         while left < right:
#             while left < right and not regex.sub('', s[left]): left += 1
#             while left < right and not regex.sub('', s[right]): right -= 1
                                
#             while left < right and not re.match('^[a-zA-Z0-9]', s[left]): left += 1
#             while left < right and not re.match('^[a-zA-Z0-9]', s[left]): right -= 1


#         left, right = 0, len(s)-1
#         while left < right:
#             while left < right and not self.alphaNum(s[left]):
#                 left += 1
#             while right > left and not self.alphaNum(s[right]):
#                 right -= 1
#             if s[left].lower() != s[right].lower():
#                 return False
#             left, right = left+1, right-1
#         return True

#     def alphaNum(self, c):
#         return (ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'))