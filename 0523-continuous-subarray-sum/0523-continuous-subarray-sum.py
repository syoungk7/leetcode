class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## Time: O(N), Space: O(K)

        hash_map = {0: 0}
        summa = 0
        tmp = 0
        # for idx, val in enumerate(nums):
        for idx in range(len(nums)):
            summa += nums[idx]
            if summa % k in hash_map and (idx+1) - hash_map[summa % k] >= 2:
                    return True
            elif summa % k not in hash_map: 
                hash_map[summa % k] = idx+1
    
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
    
