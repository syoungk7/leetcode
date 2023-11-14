class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## Time: O(N), Space: O(K)

        hash_map = {0: 0}
        summa = 0
        # for idx, val in enumerate(nums):
        for idx in range(len(nums)):
            summa += nums[idx]
            if summa % k in hash_map and (idx+1) - hash_map[summa % k] >= 2:
                    return True
            elif summa % k not in hash_map: 
                hash_map[summa % k] = idx+1

        return False