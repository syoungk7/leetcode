class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr = arr1 + arr2 + arr3
        prev, count = -1, 0
        new = []
        
        for i in sorted(arr):
            if i == prev:
                count += 1
                if count == 3:
                    new.append(i)
            if i > prev:
                prev = i
                count = 1
        return new