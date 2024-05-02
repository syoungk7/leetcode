class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         left = 0

#         for right in range(1, len(nums)):
#             if nums[right] != 0 and nums[left] == 0:
#                 nums[left], nums[right] = nums[right], nums[left]

#             # wait while we find a non-zero element to swap with you
#             if nums[left] != 0:
#                 left += 1
        
        count = 0
        for i in nums:
            if i != 0:
                nums[count] = i
                count += 1
        
        for i in range(count, len(nums)):
            nums[i] = 0