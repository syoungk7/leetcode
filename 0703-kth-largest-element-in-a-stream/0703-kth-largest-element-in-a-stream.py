class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        
        # initialize a heap with k-length
        if len(self.nums) != k:
            while len(self.nums) > k:
                heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # add val
        heapq.heappush(self.nums, val)
        # remove smallest
        if len(self.nums) != self.k:
            heapq.heappop(self.nums)
        # return heapq.nsmallest(1, self.nums)[0]
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)