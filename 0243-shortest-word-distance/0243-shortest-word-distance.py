class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx, word2_idx = [], []
        
        for idx, word in enumerate(wordsDict):
            word1_idx.append(idx) if word == word1 else None
            word2_idx.append(idx) if word == word2 else None

        return min(abs(a-b) for a in word1_idx for b in word2_idx)