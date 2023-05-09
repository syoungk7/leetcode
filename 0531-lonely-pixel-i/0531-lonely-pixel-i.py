class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count = 0
        for i in picture:
            count_row = sum(1 for j in i if j == 'B')
            if count_row == 1:
                count_col = sum(1 for k in picture if k[i.index("B")] == 'B')
                if count_col == 1:
                    count += 1
        return count