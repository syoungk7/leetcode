class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i-1] == 0 or num[i-1] > nums[i]:
        #         nums[i-1], nums[i] = nums[i], nums[i-1]
        #     print(nums) 
#         left = 0

#         for right in range(len(nums)):
#             if nums[right] != 0:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 left += 1
#             print(nums)
        
#         return nums
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1