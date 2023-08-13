class Solution:
    def countLetters(self, s: str) -> int:
        summ = 0

        for idx in range(len(s)):
            if idx == 0:
                count = 1
            elif s[idx-1] == s[idx]:
                count += 1
            else:
                count = 1
            summ += count

        return summ