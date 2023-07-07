class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #lst2 = list(zip(word1, word2))
        #comb_word = "".join([str("".join(i)) for i in lst2])
        comb_word = ""
        leng = min(len(word1), len(word2))
        
        for i in range(leng):
            comb_word += word1[i]
            comb_word += word2[i]
        
        if len(word1) != len(word2):
            if len(word1) > len(word2):
                comb_word += word1[leng::]
            else:
                comb_word += word2[leng::]

        return comb_word