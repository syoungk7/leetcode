class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        nums1_vals = nums1[:m]
        
        for k in range(m+n):

            if n <= j or (i < m and nums1_vals[i] <= nums2[j]):                 
                nums1[k] = nums1_vals[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

        # nums1[m::] = nums2
        # nums1 = nums1.sort()