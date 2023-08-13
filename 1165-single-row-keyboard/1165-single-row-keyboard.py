class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        btime, ttime = 0, 0
        
        for i in word:
            ttime += abs(keyboard.index(i) - btime)
            btime = keyboard.index(i)
        
        return ttime