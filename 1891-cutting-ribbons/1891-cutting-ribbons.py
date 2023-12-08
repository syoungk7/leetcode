class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 1
        right = max(ribbons)
        
        while(left <= right):
            mid = left + (right - left) // 2
            num_of_ribbon = 0

            for i in ribbons:
                num_of_ribbon += i // mid

            if num_of_ribbon >= k:
                left = mid + 1
            else:
                right = mid - 1

        return right