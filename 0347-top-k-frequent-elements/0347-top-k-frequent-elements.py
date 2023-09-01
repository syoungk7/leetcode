class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp_dic = dict()
        out = []
        for num in nums:
            if num not in tmp_dic:
                tmp_dic[num] = 1
            else:
                tmp_dic[num] += 1

        tmp_dic = sorted(tmp_dic.items(), key=lambda x: x[1], reverse=True)
        print(tmp_dic)
        for i in range(k): out.append(tmp_dic[i][0])
        
        return out
        
        
        