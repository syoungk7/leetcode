class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word

        return word[word.index(ch)::-1] + word[word.index(ch)+1::]
           
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word: return word
    
#         i = word.index(ch)
#         z = word[i::-1]
#         return z + word[i+1::]