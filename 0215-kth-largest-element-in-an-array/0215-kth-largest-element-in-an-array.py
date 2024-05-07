class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]
#         heap = []
        
#         for num in nums:
#             if len(heap) < k:
#                 heapq.heappush(heap, num)
#             else:
#                 heapq.heappushpop(heap, num)
#         return heapq.heappop(heap)
        
    
        