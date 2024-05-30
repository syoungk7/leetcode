class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = [i for i in magazine]
        print(tmp)
        for i in ransomNote:
            
            if i in tmp:
                tmp.pop(tmp.index(i))
            else:
                return False
        return True