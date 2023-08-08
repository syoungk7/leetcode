class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        arr = sorted(arr)
# #         if arr is None:
# #             return 0
        print(len(arr))
        for i in range(0, len(arr)):
            if arr[i]+1 in arr:
                count += 1
        return count