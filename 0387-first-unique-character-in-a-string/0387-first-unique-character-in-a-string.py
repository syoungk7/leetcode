class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = []
        for idx, char in enumerate(s):
            if char not in s[idx+1::] and char not in seen:
                return idx
            else:
                seen.append(char)
        return -1