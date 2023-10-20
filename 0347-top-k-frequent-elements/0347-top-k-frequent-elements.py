class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0: return []
        
        uniq = set(nums)
        
        from collections import defaultdict 
        count_nums = defaultdict()
        
        for i in nums:
            if i in count_nums:
                count_nums[i] += 1
            else:
                count_nums[i] = 1

        return [key for key, val in sorted(count_nums.items(), key=lambda item: item[1], reverse = True)][0:k]
