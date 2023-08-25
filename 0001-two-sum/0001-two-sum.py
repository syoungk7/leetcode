class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        
        for num in nums:
            if target >= 0 and num <= target:
                for idx, num2 in enumerate(nums):
                    if num + num2 == target and nums.index(num) != idx:
                        return [nums.index(num), idx]
                        
            elif target < 0 and num >= target:
                for idx, num2 in enumerate(nums):
                    if num + num2 == target and nums.index(num) != idx:
                        return [nums.index(num), idx]                
            