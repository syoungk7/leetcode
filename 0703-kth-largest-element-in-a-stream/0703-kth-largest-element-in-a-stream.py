class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize variables
        self.k = k
        self.nums = nums
        
        # Heap structure -> ordered list
        heapq.heapify(self.nums)
        
        # Adjust the length of heap at k
        if len(self.nums) != k:
            while len(self.nums) > k:
                heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Add new integer (ordered)
        heapq.heappush(self.nums, val)
        
        
        # Keep the same length by removing the smallest(first) integer
        if len(self.nums) != self.k:
            heapq.heappop(self.nums)
        
        # Return first(k-th smallest) interger
        return self.nums[0]

# The heapify(iterable):- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
# heappush(heap, ele): This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.
# heappop(heap): This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)