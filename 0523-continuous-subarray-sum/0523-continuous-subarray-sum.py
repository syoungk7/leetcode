class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## Time: O(N), Space: O(K)

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