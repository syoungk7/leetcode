class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse=True)
        
        while len(stones) > 1:
            y = stones[0]
            x = stones[1]
            
            if y == x:
                stones = stones[2::]
            else:
                stones = stones[2::]
                stones.append(y-x)
                stones = sorted(stones, reverse=True)
                
        if len(stones) == 0: return 0
        else:
            return stones[0]