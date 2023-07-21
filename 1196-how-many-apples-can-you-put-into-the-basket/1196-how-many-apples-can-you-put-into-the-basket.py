class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight = sorted(weight)
        if len(weight) == 1:
            return len(weight)
        
        summ = 0
        for idx, w in enumerate(weight):
            summ += w
            print(idx, w)
            if summ > 5000:
                return idx
        return len(weight)
                