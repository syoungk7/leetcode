class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new = []
        
        for i in nums1:
            new.append(nums2.index(i))
            
        return new