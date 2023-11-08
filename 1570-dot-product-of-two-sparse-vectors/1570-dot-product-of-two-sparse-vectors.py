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
        if len(self.sv) > len(vec.sv):
            for key in vec.sv.keys():
                if key in self.sv:
                    output += self.sv[key] * vec.sv[key]
        else:
             for key in self.sv.keys():
                if key in vec.sv:
                    output += self.sv[key] * vec.sv[key]           
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)