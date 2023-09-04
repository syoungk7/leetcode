class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 3 and sum(nums) == 0: return [nums]
        
#         tmp = sorted(nums)
#         tmp_i, tmp_j, tmp_k = [], [], []
#         out = set()
        
#         for num in nums:
#             if num < 0: tmp_i.append(num)
#             elif num == 0: tmp_j.append(num)
#             else: tmp_k.append(num)
#         #print(tmp_i, tmp_j, tmp_k)
                
#         if len(tmp_j) >= 3: 
#             out.add(tuple(tmp_j[0:3]))
        
#         if tmp_j:
#             for j in tmp_i:
#                 if -j in tmp_k: out.add((j, 0, -j))

#         for i in range(len(tmp_i)-1):
#             for ii in range(i+1, len(tmp_i)):
#                 if -(tmp_i[i] + tmp_i[ii]) in tmp_k:
#                     tuple_ = (tmp_i[i], tmp_i[ii], -(tmp_i[i] + tmp_i[ii]))   
#                     out.add(tuple(sorted(tuple_)))
        
#         for k in range(len(tmp_k)-1):
#             for kk in range(k+1, len(tmp_k)):
#                 if -(tmp_k[k] + tmp_k[kk]) in tmp_i:
#                     tuple_ = (-(tmp_k[k] + tmp_k[kk]), tmp_k[k], tmp_k[kk])  
#                     out.add(tuple(sorted(tuple_)))
        
#         return list(out)

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
