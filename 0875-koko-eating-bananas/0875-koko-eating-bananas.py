class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            middle = (left + right) // 2
            cb = 0

            for i in piles:
                cb += ((i-1) // middle) + 1

            if cb > h:
                left = middle + 1
            else:
                right = middle

        return left