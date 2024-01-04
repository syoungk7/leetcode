class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        count = 0
        
        if 1 in count_nums.values(): return -1

        for i in count_nums.values():
            count += ceil(i/3)
   

        return count