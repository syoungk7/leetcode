class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = {'+': lambda i, j: i + j, '-': lambda i, j: i - j, '*': lambda i, j: i * j, '/': lambda i, j: i / j}
        stack = []

        for val in tokens:
            if stack and val in calc:
                a = stack.pop()
                stack.append(int(calc[val](stack.pop(), a)))
            else:
                stack.append(int(val))
        return stack[0]