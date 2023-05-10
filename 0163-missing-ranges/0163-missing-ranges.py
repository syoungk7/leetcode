class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        new = []
     
        if len(nums) == 0:
            new.append([lower, upper])
            return new

        elif nums[0] > lower:
            new.append([lower, nums[0]-1])

        for leng in range(0, len(nums)-1):
            if nums[leng+1] - nums[leng] <= 1:
                continue
            else:
                new.append([nums[leng]+1, nums[leng+1]-1])


        if nums[-1] < upper:
            new.append([(nums[-1])+1, upper])

        return new