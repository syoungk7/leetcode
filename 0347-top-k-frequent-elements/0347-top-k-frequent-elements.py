class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp_dic = dict()

        # count nums
        for num in nums:
            if num not in tmp_dic:
                tmp_dic[num] = 1
            else:
                tmp_dic[num] += 1

        # sort
        tmp_dic = sorted(tmp_dic.items(), key=lambda x: x[1], reverse=True)
        
        return [tmp_dic[i][0] for i in range(k)]

# collections.Counter & heaoq    
#         tmp = collections.Counter(A)
#         nums = list(tmp.keys())
#         res = [(-float("inf"), 0)]*k
#         heapq.heapify(res)
#         for num in nums:
#             if tmp[num] > res[0][0]:
#                 heapq.heapreplace(res, (tmp[num], num))
#         return [i[1] for i in res]
        