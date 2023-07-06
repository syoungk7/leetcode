class Solution:
    def isArmstrong(self, n: int) -> bool:
        if type(n) is not int:
            return False

        summa = 0
        for i in str(n):
            summa += int(i)**len(str(n))
        
        return n == summa