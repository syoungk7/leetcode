class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x ** n
        e = -n if n < 0 else n
        res = 1.0
        mult = 1 / x if n < 0 else x
        while e != 0:
            if e & 1:
                res *= mult
            mult *= mult
            e >>= 1
        return res