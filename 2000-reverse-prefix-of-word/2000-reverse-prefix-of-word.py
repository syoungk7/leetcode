class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            rev_idx = word.index(ch)+1
            return word[0:rev_idx][::-1] + word[rev_idx::]
        else:
            return word
        