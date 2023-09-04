class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         pair = defaultdict()
        
#         for i in range(len(numbers)):
            
#             if numbers[i] == target/2 and numbers[i] == numbers[i+1]:
#                 return [i+1, i+2]
            
#             elif numbers[i] != target/2 and numbers[i] not in pair:
#                 pair[numbers[i]] = i+1
            
#             if target - numbers[i] in pair:
#                 return [pair[target - numbers[i]], i+1]
            
        dic = {}
        
        for idx, val in enumerate(numbers):
            
            if target-val in dic: return [dic[target-val], idx + 1]
            
            dic[val] = idx + 1