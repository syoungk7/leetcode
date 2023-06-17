class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        for idx in range(len(nums)-1):
            missing = nums[idx+1] - nums[idx] -1
            if missing < k:
                k = k - missing
                continue
            else:
                return nums[idx] + k
            
        return nums[-1] + k
            
                
                