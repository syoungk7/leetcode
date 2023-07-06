class Solution:
    def isArmstrong(self, n: int) -> bool:
        if type(n) is not int:
            return False

        str_n = str(n)
        len_n = len(str_n)
        summa = 0
        for i in str_n:
            summa += int(i)** len_n
        
        return n == summa