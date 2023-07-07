class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        map_tf = collections.Counter()
        ans, lef = k, 0
        
        for rig in range(len(answerKey)):
            map_tf[answerKey[rig]] += 1
            
            while map_tf['F'] > k and map_tf['T'] > k:
                map_tf[answerKey[lef]] -= 1
                lef += 1
            ans = max(ans, rig-lef+1)
            
        return ans
