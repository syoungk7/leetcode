class Solution:
    def isPalindrome(self, s: str) -> bool:
        #tmp = ''.join([char for char in s if char.isalpha() or char.isnumeric()]).lower()
        tmp = ''.join([char for char in s if char.isalnum()]).lower()

        print(tmp)
        return tmp == tmp[::-1]