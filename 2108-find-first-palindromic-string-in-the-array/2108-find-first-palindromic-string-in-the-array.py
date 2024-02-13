class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            length = len(word)
            left, right = 0, len(word)
            while left < right:
                if word[left] != word[right-1]:
                    break
                left += 1
                right -= 1
            else: 
                return word
        return ""
#         for word in words:
#             if word == word[::-1]:
#                 return word

#         return ""
    
#         for word in words:
#             i, j = 0, len(word) - 1
#             while i < j:
#                 if word[i] != word[j]: break
#                 i += 1
#                 j -= 1
#             else: return word
#         return ""