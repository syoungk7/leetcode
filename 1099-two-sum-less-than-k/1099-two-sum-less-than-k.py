class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        new = [i for i in nums if i < k]
        maxx = 0
        if len(new) < 2 : return -1

        for i in range(len(new)):
            for j in range(len(new)):
                if i != j and new[i]+new[j] < k: 
                    maxx = max(maxx, new[i]+new[j])

        if maxx > k: return -1

        return maxx
        
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
        