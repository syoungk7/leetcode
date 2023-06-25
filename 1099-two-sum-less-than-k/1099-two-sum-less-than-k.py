class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        import itertools
        lst = []
        for i in itertools.permutations(nums, 2):
            if sum(i) < k:
                lst.append(sum(i))
        if len(lst) == 0:
            return -1
        else:
            new = sorted(lst)
        
        return new[-1]
        