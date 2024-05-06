class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        merged_str = ''
        
        while i < len(word1) or j < len(word2):

            if i < len(word1):
                merged_str += word1[i]
                i += 1
        
            if j < len(word2):
                merged_str += word2[j]
                j += 1
     
        return merged_str