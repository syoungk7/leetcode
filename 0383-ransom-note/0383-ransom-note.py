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

        m_counts = collections.Counter(magazine)
        r_counts = collections.Counter(ransomNote)

        for idx, val in r_counts.items():
            m_count = m_counts[idx]
            if m_count < val:
                return False
        return True