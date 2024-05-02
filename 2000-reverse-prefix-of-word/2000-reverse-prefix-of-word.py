class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word

        rev_idx = word.index(ch)
        rev = word[rev_idx::-1]
        return rev + word[rev_idx+1::]
           
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word: return word
    
#         i = word.index(ch)
#         z = word[i::-1]
#         return z + word[i+1::]
        # ind = list(word).index(ch)
        # l = (word[:ind+1][::-1])
        # word = list(word)
        # word[:ind+1] = l
        # return "".join(word)