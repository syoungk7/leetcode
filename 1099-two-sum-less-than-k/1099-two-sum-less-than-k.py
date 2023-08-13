class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        new = sorted(nums)
        if len(new) < 2 : return -1
        if new[0]+new[1] > k: return -1
        
        left, right, maxx = 0, len(new)-1, 0
        while left < right:
            summ = new[left] + new[right]
            if summ < k:
                maxx = max(maxx, summ)
                left += 1
            if summ >= k:
                right -= 1
                       
        return maxx
        
#         import itertools
#         lst = []
#         for i in itertools.permutations(nums, 2):
#             if sum(i) < k:
#                 lst.append(sum(i))
#         if len(lst) == 0:
#             return -1
#         else:
#             new = sorted(lst)
        
#         return new[-1]
        