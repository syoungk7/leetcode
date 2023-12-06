class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j or nums[i] > k or nums[j] > k or nums[i] + nums[j] > k:
                    pass
                else:
                    if nums[i] + nums[j] > max_sum and nums[i] + nums[j] < k:
                        max_sum = nums[i] + nums[j]
        if max_sum != 0:
            return max_sum
        else:
            return -1