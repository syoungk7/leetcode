class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x ** n
        if n == 0: return 1.0
        if n == 1: return x

        new_n = abs(n)
        new_x = x if n > 0 else 1/x
        mul_x = 1

        while new_n != 0:
            if new_n % 2 == 1:
                mul_x *= new_x
                new_n -= 1
            new_x *= new_x
            new_n //= 2

        return mul_x
    
        # e = -n if n < 0 else n
        # res = 1.0
        # mult = 1 / x if n < 0 else x
        # while e != 0:
        #     if e & 1:
        #         res *= mult
        #     mult *= mult
        #     e >>= 1
        # return res