class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0
        
        for i in nums:
            if i == target: count += 1
                
        if count > len(nums)/2: return True
        
        return False