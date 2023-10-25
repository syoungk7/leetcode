class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True        
        s = "".join(re.split("[^a-zA-Z0-9]*", s.lower()))

        return s == s[::-1]
    
        # s = [char.lower() for char in s if char.isalpha() == True or char.isdigit() == True]
        # A = ''.join(s)
        # s.reverse()
        # return A == ''.join(s)
