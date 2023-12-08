class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num)-1

        while idx >= 0:
            if int(num[idx]) % 2:
                return num[:idx+1]
            idx -= 1

        return ""

