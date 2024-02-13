class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # for word in words:
        #     length = len(word)
        #     left, right = 0, len(word)
        #     while left < right:
        #         if word[left] == word[right-1]:
        #             left += 1
        #             right -= 1
        #         else:
        #             continue
        #     if word[left] == word[right-1]:
        #         return word
        # else:
        #     return ""
        for word in words:

            if word == word[::-1]:
                return word

        return ""