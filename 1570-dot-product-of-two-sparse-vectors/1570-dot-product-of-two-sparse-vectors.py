class SparseVector:
    def __init__(self, nums):
        self.q = [(i, n) for i, n in enumerate(nums) if n != 0]


        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        res = 0
        p1, p2 = 0, 0
        while p1 < len(self.q) and p2 < len(vec.q):
            i1, v1 = self.q[p1]
            i2, v2 = vec.q[p2]
            if i1 == i2:
                res += v1 * v2
                p1 += 1
                p2 += 1
            elif i1 > i2:
                p2 += 1
            else:
                p1 += 1
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)