class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # reverse nums to use heapq's pop (smallest)
        rev_stone = [-stone for stone in stones]
        heapq.heapify(rev_stone)
        
        if len(rev_stone) != 1:
            while len(rev_stone) != 1:
                # diff = heapq.heappop(rev_stone) - heapq.heappop(rev_stone)
                # heapq.heappush(rev_stone, diff)
                heapq.heappush(rev_stone, heapq.heappop(rev_stone) - heapq.heappop(rev_stone))
        return -rev_stone[0]