class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp_dic = {}
        
        for idx, val in enumerate(numbers):
            
            if target - val in tmp_dic: 
                return [tmp_dic[target - val], idx + 1]
            
            tmp_dic[val] = idx + 1        