class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx, word2_idx = [], []
        
        for idx, word in enumerate(wordsDict):
            if word == word1:
                word1_idx.append(idx)
            if word == word2:
                word2_idx.append(idx)
        return min(abs(a-b) for a in word1_idx for b in word2_idx)