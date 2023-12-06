class Solution:
    def totalMoney(self, n: int) -> int:
        init = 0
        saving = 0

        for i in range(n):
            if i % 7 == 0:
                init += 1
                saving += init + (i % 7)
            else:
                saving += init + (i % 7)
        return saving