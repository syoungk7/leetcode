class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1: return True
        
        s = [char.lower() for char in s if char.isalpha() == True or char.isdigit() == True]

        A = ''.join(s)
        s.reverse()

        return A == ''.join(s)
        