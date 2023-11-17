class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ## TC: O(N), SC(1)
        # if target in nums: 
        #     return nums.index(target)
        # else: 
        #     return -1
        
        ## TC: O(logN?, worst -> N), SC(1)
        # if target in nums[0:int(len(nums)/2)]: 
        #     return nums.index(target)
        # elif target in nums[int(len(nums)/2)::]:
        #     return nums.index(target)
        # else: 
        #     return -1
        
        ## nums: sorted in ascending order
        ## TC: O(logN), SC(1)
        start, end = 0, len(nums) - 1 ## index

        while start <= end:
            middle = int((start + end)/2)

            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                return middle
        return -1