class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        arr = sorted(arr)

        for i in range(len(arr)):
            if arr[i]+1 in arr:
                count += 1
        return count
