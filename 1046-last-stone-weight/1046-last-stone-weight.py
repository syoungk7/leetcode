class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#         stones.sort()
#         while len(stones) > 1:
#             stone_1 = stones.pop()
#             stone_2 = stones.pop()
#             if stone_1 != stone_2:
#                 bisect.insort(stones, stone_1 - stone_2)
#         return stones[0] if stones else 0
    
    
        rev_stone = [-stone for stone in stones]
        heapq.heapify(rev_stone)
        while (len(rev_stone)) > 1:
            heapq.heappush(rev_stone, heapq.heappop(rev_stone) - heapq.heappop(rev_stone))
        return -rev_stone[0]