class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## nums: sorted in ascending order
        ## TC: O(logN), SC(1)
        if target <= nums[0]: return 0
        if target == nums[-1]: return len(nums) -1
        if target > nums[-1]: return len(nums)
        
        start, end = 0, len(nums) - 1 ## index

        while start <= end:
            middle = int((start + end)/2)

            if nums[middle] < target:
                start += 1
            elif nums[middle] > target:
                end -= 1
            else:
                if nums[middle] == target:
                    return middle

        return start