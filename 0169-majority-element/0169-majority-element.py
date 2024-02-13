class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## TC On, SC On
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
    
        # ## TC On^2, SC O1
        # half = len(nums) // 2
        # for num in nums:
        #     counts = sum(1 for same in nums if num == same)
        #     if counts > half:
        #         return num
        # time limit exceeded

        ## TC Onlogn, SC O1
        return sorted(nums)[len(nums) // 2]
        