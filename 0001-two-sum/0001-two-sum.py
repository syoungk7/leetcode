class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #if len(nums) < 2: return []

        

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []
                
# solution using diff        
        pair = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            
            if diff in pair:
                return pair[diff], idx
            
            pair[nums[idx]] = idx

# solution using loop
#         for num in nums:
#             if target >= 0 and num <= target:
#                 for idx, num2 in enumerate(nums):
#                     if num + num2 == target and nums.index(num) != idx:
#                         return [nums.index(num), idx]
                        
#             elif target < 0 and num >= target:
#                 for idx, num2 in enumerate(nums):
#                     if num + num2 == target and nums.index(num) != idx:
#                         return [nums.index(num), idx]                
            