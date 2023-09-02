class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        if n == 0: return out
        
        for i in range(1, n+1):
            tmp = 0
            #print(list(str(format(i, 'b'))))
            for j in list(str(format(i, 'b'))):
                if int(j) == 1:
                    tmp += 1
            out.append(tmp)
        return out
            
        