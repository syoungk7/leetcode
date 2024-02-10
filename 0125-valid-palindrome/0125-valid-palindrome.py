class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # #tmp = ''.join([char for char in s if char.isalpha() or char.isnumeric()]).lower()
        # tmp = ''.join([char for char in s if char.isalnum()]).lower()
        # # print(tmp)
        # return tmp == tmp[::-1]

        ## two points
        left, right = 0, len(s)-1
        regex = re.compile('[^a-zA-Z0-9]')

        while left < right:
            print(regex.sub('', s[left]))
            while left < right and not regex.sub('', s[left]): left += 1
            while left < right and not regex.sub('', s[right]): right -= 1
            if s[left].lower() != s[right].lower(): return False

            left += 1
            right -= 1
        return True