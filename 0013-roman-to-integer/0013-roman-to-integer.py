class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        values2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        output = 0

        for idx, sym in enumerate(s):
            if s[idx:idx+1] and s[idx:idx+2] in values2:
                output += values2[s[idx:idx+2]]
                output -= values[s[idx+1]]
            else:
                output += values[sym]
    
        return output