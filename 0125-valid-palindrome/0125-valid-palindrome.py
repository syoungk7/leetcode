class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #tmp = ''.join([char for char in s if char.isalpha() or char.isnumeric()]).lower()
        # tmp = ''.join([char for char in s if char.isalnum()]).lower()
        # print(tmp)
        # return tmp == tmp[::-1]
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]