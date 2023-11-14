class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for par in s:
            if par == '(':
                stack.append(par)
            elif stack and par == ')':
                stack.pop()
            elif not stack and par == ')':
                count += 1

        return len(stack) + count