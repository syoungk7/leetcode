class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## Time: O(N), Space: O(K)
        if len(nums) < 2: return False

        hash_map = {0: 0}
        summa = 0
        
        for idx, val in enumerate(nums):
            summa += val
            if summa % k in hash_map:
                if hash_map[summa % k] < idx:
                    return True
            else:
                hash_map[summa % k] = idx + 1
    
        return False


#         s = nums[0]
#         lagging_s = 0
#         subsums = {0: 1}
#         for i in range(1, len(nums)):
#             s += nums[i]
#             s = s % k
#             if s in subsums:
#                 return True
#             lagging_s = (lagging_s + nums[i - 1]) % k
#             subsums[lagging_s] = 1
#         return False
    
