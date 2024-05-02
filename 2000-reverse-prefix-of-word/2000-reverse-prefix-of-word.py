class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word

        rev_idx = word.index(ch)
        return word[rev_idx::-1] + word[rev_idx+1::]
           
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word: return word
    
#         i = word.index(ch)
#         z = word[i::-1]
#         return z + word[i+1::]