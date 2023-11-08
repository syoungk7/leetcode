class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sv = {}
        for idx, val in enumerate(nums):
            if val != 0:
                self.sv[idx] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        output = 0
        shared_key = set(self.sv.keys()).intersection(set(vec.sv.keys()))

        for key in shared_key:
            output += self.sv[key] * vec.sv[key]           
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)