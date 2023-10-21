class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x ** n

#         new_n = n if n > 0 else -n
#         new_x = x if n > 0 else 1/x
#         mul_x = 1

#         while n != 0:
#             if n & 1:
#                 mul_x *= new_x
#             new_x *= new_x
#             n >>= 1

#         return mul_x
    
        e = -n if n < 0 else n
        res = 1.0
        mult = 1 / x if n < 0 else x
        while e != 0:
            if e & 1:
                res *= mult
            mult *= mult
            e >>= 1
        return res