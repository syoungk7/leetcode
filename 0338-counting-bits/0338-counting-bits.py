class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        if n == 0: return out
        
        for i in range(1, n+1):
            tmp = format(i, 'b').count('1')
            out.append(tmp)
        return out
            
#         dp = [0] * (n+1)
#         for i in range(n+1):
#             dp[i] = dp[i//2] + i % 2
        
#         return dp

        # a = []
        # for i in range(n+1):
        #     b = bin(i)[2:].count('1')
        #     a.append(b)
        # return a