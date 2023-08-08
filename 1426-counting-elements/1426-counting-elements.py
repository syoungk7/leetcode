class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        arr = sorted(arr)
        arr2 = set(arr)

        for i in range(len(arr)):
            if arr[i]+1 in arr2:
                count += 1
        return count
