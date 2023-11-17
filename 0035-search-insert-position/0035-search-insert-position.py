class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## nums: sorted in ascending order
        ## TC: O(logN), SC(1)
        if target <= nums[0]: return 0
        if target == nums[-1]: return len(nums)-1
        if target > nums[-1]: return len(nums)
        if len(nums) < 3:
            if target in nums: return nums.index(target)
            else: return 1
        
        right, left = 0, len(nums) - 1 ## index

        while right <= left:
            middle = int((right + left)/2)

            if nums[middle] < target:
                right = middle + 1
            elif nums[middle] > target:
                left = middle - 1
            else:
                if nums[middle] == target:
                    return middle
            print(right, left)
        return right