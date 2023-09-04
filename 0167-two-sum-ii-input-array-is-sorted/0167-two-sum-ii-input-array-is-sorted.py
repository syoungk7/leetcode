class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         tmp_dic = defaultdict()
        
#         for i in range(len(numbers)):
            
#             if numbers[i] == target/2 and numbers[i] == numbers[i+1]:
#                 return [i+1, i+2]
            
#             elif numbers[i] != target/2 and numbers[i] not in tmp_dic:
#                 tmp_dic[numbers[i]] = i+1
            
#             if target - numbers[i] in tmp_dic:
#                 return [tmp_dic[target - numbers[i]], i+1]
            
        tmp_dic = {}
        
        for idx, val in enumerate(numbers):
            
            if target - val in tmp_dic: 
                return [tmp_dic[target - val], idx + 1]
            
            tmp_dic[val] = idx + 1