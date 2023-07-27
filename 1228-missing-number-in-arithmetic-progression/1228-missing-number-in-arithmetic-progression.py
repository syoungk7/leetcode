class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        m, pre = len(arr), 0
        arr = sorted(arr)
        
        if len(set(arr)) == 1:
            return arr[0]
        
        for i in range(round(m/2)+1):
            left = arr[i+1] - arr[i]
            right = arr[m-(i+1)] - arr[m-(i+2)]
            print(left, right)
            if left > right: return int(arr[i] + left/2)
            elif left < right: return int(arr[m-(i+2)] + right/2)
            
            if pre != 0 and pre != left: return int(arr[i] + left/2)
            
            pre = left
