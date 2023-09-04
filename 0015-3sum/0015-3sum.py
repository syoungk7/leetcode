class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0: return [nums]
        
        tmp = sorted(nums)
        tmp_i, tmp_j, tmp_k = [], [], []
        out = set()
        
        for num in nums:
            if num < 0: tmp_i.append(num)
            elif num == 0: tmp_j.append(num)
            else: tmp_k.append(num)
        #print(tmp_i, tmp_j, tmp_k)
        set_i, set_k = set(tmp_i), set(tmp_k)
                
        if len(tmp_j) >= 3: 
            out.add(tuple(tmp_j[0:3]))
        
        if tmp_j:
            for j in tmp_i:
                if -j in set_k: out.add((j, 0, -j))

        for i in range(len(tmp_i)-1):
            for ii in range(i+1, len(tmp_i)):
                if -(tmp_i[i] + tmp_i[ii]) in set_k:
                    tuple_ = (tmp_i[i], tmp_i[ii], -(tmp_i[i] + tmp_i[ii]))   
                    out.add(tuple(sorted(tuple_)))
        
        for k in range(len(tmp_k)-1):
            for kk in range(k+1, len(tmp_k)):
                if -(tmp_k[k] + tmp_k[kk]) in set_i:
                    tuple_ = (-(tmp_k[k] + tmp_k[kk]), tmp_k[k], tmp_k[kk])  
                    out.add(tuple(sorted(tuple_)))
        
        return list(out)