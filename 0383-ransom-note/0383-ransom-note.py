class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         tmp = [i for i in magazine]

#         for i in ransomNote:
#             if i in tmp:
#                 tmp.pop(tmp.index(i))
#             else:
#                 return False
#         return True

        if len(ransomNote) > len(magazine): return False

        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)

        for char, count in ransom_note_counts.items():
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
        return True