class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True

        tmp = "".join(re.split("[^a-zA-Z0-9]*", s.lower()))
        
        return tmp == tmp[::-1]
