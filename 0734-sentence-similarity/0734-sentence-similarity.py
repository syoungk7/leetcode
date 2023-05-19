class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        if len(sentence1) == len(sentence2):
            for i, j in zip(sentence1, sentence2):
                #print([i, j], [j, i])
                if i == j:
                    continue
                elif [i, j] in similarPairs or [j, i] in similarPairs :
                    continue
                else:
                    return False
        return True