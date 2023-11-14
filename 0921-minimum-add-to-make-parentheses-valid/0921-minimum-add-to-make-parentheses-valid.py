class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        curr = 0
        for par in s:
            if par == '(':
                count += 1
                curr += 1
            elif curr != 0 and par == ')':
                count -= 1
                curr -= 1
            elif curr == 0 and par == ')':
                count += 1

        return abs(count)