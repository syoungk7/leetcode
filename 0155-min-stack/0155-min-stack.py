class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini = min(self.stack)

    def pop(self) -> None:
        p = self.stack.pop()
        if self.stack:
            self.mini = min(self.stack)
        return p
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
