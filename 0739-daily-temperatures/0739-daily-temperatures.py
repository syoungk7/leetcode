class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                a = stack.pop()
                out[a] = idx - a
            stack.append(idx)
        return out