class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) != len(set(nums)):
        #     return True
        # else: return False
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False