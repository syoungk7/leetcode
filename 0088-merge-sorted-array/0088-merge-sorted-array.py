class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ## TC - O(k), SC - O(m)
        i = j = 0
        nums1_vals = nums1[:m]
        
        for k in range(m+n):

            if n == j or (i < m and nums1_vals[i] <= nums2[j]):                 
                nums1[k] = nums1_vals[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

        ## TC - sorting - O(klogk), SC - O(n)
        # nums1[m::] = nums2
        # nums1 = nums1.sort()
        
        ## TC - O(k), SC - O(1)
        # i = m - 1
        # j = n - 1
        # for k in range(n + m-1, -1, -1):
        #     if j < 0:
        #         break
        #     if i >= 0 and nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1