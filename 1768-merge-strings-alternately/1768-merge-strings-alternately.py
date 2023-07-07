class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst2 = list(zip(word1, word2))
        comb_word = "".join([str("".join(i)) for i in lst2])
        
        if len(word1) != len(word2):
            if len(word1) > len(word2):
                comb_word = comb_word + word1[len(word2)::]
            else:
                comb_word = comb_word + word2[len(word1)::]
        return comb_word
        