class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for i, j in shift:
            if j > len(s): j = j % len(s)
    
            if i == 0: new = s[j::] + s[0:j]
            if i == 1: new = s[len(s)-j::] + s[0:len(s)-j]
            s = new

        return new