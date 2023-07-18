class Solution:
    def countLetters(self, s: str) -> int:
        lst = []
        letter = '0'
        intial = s[0]
        for idx, val in enumerate(s):
            if s[idx] == letter[0]:
                letter = letter + s[idx]
            else:
                lst.append(letter)
                letter = ''
                letter = s[idx]
        lst.append(letter)
        lst.pop(0)
        
        summ = 0
        for i in lst:
            if len(i) == 1:
                summ += 1
            else:
                count = 1
                while count < len(i):
                    summ += count
                    count += 1
                summ += count
        return summ