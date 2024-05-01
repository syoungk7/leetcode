class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize variables
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        
        # Adjust the length of heap at k
        if len(self.nums) != k:
            while len(self.nums) > k:
                heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Add new integer
        heapq.heappush(self.nums, val)
        
        
        # Keep the same length by removing the smallest(first) integer
        if len(self.nums) != self.k:
            heapq.heappop(self.nums)
        
        # Return first(k-th smallest) interger
        return self.nums[0]


    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)