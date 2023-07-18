class Solution:
    def countLetters(self, s: str) -> int:
        count, summ = 0, 0
        ss = '0' + s
        for idx in range(len(ss)-1):
            if ss[idx] == ss[idx+1]:
                count += 1
            else:
                count = 1
            summ += count
        return summ
    

#         count = 1
#         res = 1
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 count +=1
#             else:
#                 count = 1
#             res += count
#         return res