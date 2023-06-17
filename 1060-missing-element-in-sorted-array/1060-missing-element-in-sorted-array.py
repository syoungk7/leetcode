class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        for idx in range(len(nums)-1):
            missing = nums[idx+1] - nums[idx] -1
            print(idx, missing, k)
            if missing < k:
                k = k - missing
                print('new k:', k)
                continue
            else:
                return nums[idx] + k
            
        return nums[-1] + k
            
                
                