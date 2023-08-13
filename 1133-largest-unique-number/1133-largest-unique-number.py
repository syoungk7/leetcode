class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        uniq, delt = set(), set()
        
        for i in sorted(nums, reverse=True):
            if i not in uniq and i not in delt:
                uniq.add(i)
            elif i in uniq and i not in delt:
                uniq.remove(i)
                delt.add(i)
        
        if len(uniq) == 0: return -1
        
        return max(list(uniq))
