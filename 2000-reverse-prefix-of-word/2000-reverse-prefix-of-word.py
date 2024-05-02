# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word: return word
#         word = list(word)
        
#         rev_idx = word.index(ch)
#         rev = word[:rev_idx+1][::-1]
#         word[:rev_idx+1] = rev
#         return ''.join(word)
           
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word
    
        i = word.index(ch)
        z = word[i::-1]
        return z + word[i+1::]
