class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = {'+': lambda i, j: i + j, '-': lambda i, j: i - j, '*': lambda i, j: i * j, '/': lambda i, j: i / j}
        stack = []

        for idx, val in enumerate(tokens):
            if stack and val in calc:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(calc[val](b, a)))
            else:
                stack.append(int(val))
        return stack[0]