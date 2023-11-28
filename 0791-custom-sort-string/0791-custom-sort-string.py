class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counting = {}
        for i in s:
            if i not in counting:
                counting[i] = 1
            else:
                counting[i] += 1
        
        new = ''
        in_s = [i for i in order if i in s]
        
        for j in in_s:
            new += j * counting[j]
            s = s.replace(j, '')
                
                
        return new + s

        
        