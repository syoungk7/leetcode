class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        ## output: []
        

        for num in sorted(nums):
            pre = []
            for ss in subsets:
                if num % ss == 0:
                    tmp = max([subsets[ss]], key=len) | {num}
                    if len(tmp) > len(pre):
                        pre = tmp
                    else:
                        continue
                    #print(subsets, tmp)
            subsets[num] = pre
                    ## {-1: set()} {1}
                    ## {-1: set(), 1: {1}} {2}
                    ## {-1: set(), 1: {1}} {1, 2}
                    ## {-1: set(), 1: {1}, 2: {1, 2}} {3}
                    ## {-1: set(), 1: {1}, 2: {1, 2}} {1, 3}
            
        #print(subsets)
        ## {-1: set(), 1: {1}, 2: {1, 2}, 3: {1, 3}}

        return list(max(subsets.values(), key=len))