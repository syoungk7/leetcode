class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        summ = []
        if len(nums) < 2 : return -1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j: summ.append(nums[i] + nums[j])

        if min(summ) > k: return -1

        return max(m for m in summ if m < k)
        
#         for i, val in enumerate(sorted(nums, reverse = True)):
#             if val > k:
#                 continue
#             else:
                
#             pre = summ
#             summ += val
            
#             if summ > k:
#                 if i == 1 or i == 0: return -1
#                 else: return pre
#         return -1
        
        
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
        