class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    ## Time Limit Exceeded
#         nums.sort()
#         three = set()
        
#         for i in range(len(nums)-2):
#             for j in range(i+1,len(nums)-1):
#                 for k in range(j+1,len(nums)):
#                     temp = nums[i] + nums[j] + nums[k]
#                     if temp == 0:
#                         three.add((nums[i],nums[j],nums[k]))
#         return three


        if len(nums) == 3 and sum(nums) == 0: return [nums]
        
        tmp = sorted(nums)
        tmp_i, tmp_j, tmp_k = [], [], []
        out = set()
        
        for num in nums:
            if num < 0: tmp_i.append(num)
            elif num == 0: tmp_j.append(num)
            else: tmp_k.append(num)

        set_i, set_k = set(tmp_i), set(tmp_k)
                
        if len(tmp_j) >= 3: 
            out.add(tuple(tmp_j[0:3]))
        
        if tmp_j:
            for j in tmp_i:
                if -j in set_k: out.add((j, 0, -j))

        for i in range(len(tmp_i)-1):
            for ii in range(i+1, len(tmp_i)):
                inv = -(tmp_i[i] + tmp_i[ii])
                if inv in set_k:
                    out.add(tuple(sorted((tmp_i[i], tmp_i[ii], inv))))
        
        for k in range(len(tmp_k)-1):
            for kk in range(k+1, len(tmp_k)):
                inv = -(tmp_k[k] + tmp_k[kk])
                if inv in set_i:
                    out.add(tuple(sorted((inv, tmp_k[k], tmp_k[kk]))))
        
        return list(out)