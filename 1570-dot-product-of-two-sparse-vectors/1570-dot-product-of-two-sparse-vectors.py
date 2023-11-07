class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sv = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        output = 0
        if len(self.sv) == len(vec.sv):
            for i in range(len(vec.sv)):
                output += self.sv[i] * vec.sv[i]
        else:
            return None
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)