class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ## TC O(n), SC O(n)
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
    
        # ## TC O(n^2), SC O(1)
        # half = len(nums) // 2
        # for num in nums:
        #     counts = sum(1 for same in nums if num == same)
        #     if counts > half:
        #         return num
        # time limit exceeded

        # ## TC O(nlogn), SC O(1)
        # return sorted(nums)[len(nums) // 2]

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate