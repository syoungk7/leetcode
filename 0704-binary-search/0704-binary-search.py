class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # # TC: O(N), SC(1)
        # if target in nums: 
        #     return nums.index(target)
        # else: 
        #     return -1
        
         # TC: O(worst -> N), SC(1)
        if target in nums[0:int(len(nums)/2)]: 
            return nums.index(target)
        elif target in nums[int(len(nums)/2)::]:
            return nums.index(target)
        else: 
            return -1