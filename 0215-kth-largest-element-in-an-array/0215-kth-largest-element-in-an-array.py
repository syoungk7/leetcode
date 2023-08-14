class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(int(len(nums)/2))
        if int(len(nums)/2) > k: return sorted(nums, reverse = True)[k-1]
        elif int(len(nums)/2) == k: return sorted(nums, reverse = True)[k-1]
        else: 
            nums2 = sorted(nums, reverse = True)[int(len(nums)/2):k]
            print(nums2)
            return nums2[-1]