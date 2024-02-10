class Solution:
    def numWays(self, n: int, k: int) -> int:
        # n = 3
        # k = 4
        tmp = [0, k, k**2]
        while len(tmp) <= n:
            # print(tmp, tmp[-2:])
            tmp += sum(tmp[-2:]) * (k-1),
        return tmp[n]