class Solution:
    def isArmstrong(self, n: int) -> bool:
        str_n = str(n)
        len_n = len(str_n)
        summa = 0

        for i in str_n:
            summa += int(i)** len_n
        
        return n == summa