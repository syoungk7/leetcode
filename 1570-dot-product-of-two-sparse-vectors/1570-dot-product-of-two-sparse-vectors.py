class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #self.sv = {idx:val for idx, val in enumerate(nums) if val != 0}
        #self.sv = nums
        self.sv = [(idx, val) for idx, val in enumerate(nums) if val != 0]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        output = 0
        shared_key = set([key for key,_ in self.sv]).intersection(set([key for key,_ in vec.sv]))
        self.idx, vec.idx = 0, 0
        
        while len(shared_key) != 0:
            if self.sv[self.idx][0] in shared_key and vec.sv[vec.idx][0] in shared_key:
                output += self.sv[self.idx][1] * vec.sv[vec.idx][1]
                shared_key.remove(self.sv[self.idx][0])
            elif self.sv[self.idx][0] not in shared_key:
                self.idx += 1
            elif vec.sv[vec.idx][0] not in shared_key:
                vec.idx += 1

        # for idx, val in min_sv:
        #     if idx in []
        #         if idx == i:
        #             output += val * v

        # else: return None
  
        # if len(self.sv) > len(vec.sv):
        #     for key in vec.sv.keys():
        #         if key in self.sv:
        #             output += self.sv[key] * vec.sv[key]
        # else:
        #      for key in self.sv.keys():
        #         if key in vec.sv:
        #             output += self.sv[key] * vec.sv[key]  

#         shared_key = set(self.sv.keys()).intersection(set(vec.sv.keys()))

#         for key in shared_key:
#             output += self.sv[key] * vec.sv[key]
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)