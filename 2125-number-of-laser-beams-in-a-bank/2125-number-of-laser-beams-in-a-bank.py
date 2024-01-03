class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        count = 0
        for i in bank:
            row = i.count('1')
            count += prev*row
            if row:
                prev = row
        return count