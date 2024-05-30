class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        for idx, val in enumerate(nums):
            if idx == 0:
                cum_sum = val
            else:
                cum_sum += val
                nums[idx] = cum_sum
        return nums