class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
#         left = 1
#         right = max(ribbons)
        
#         while(left <= right):
#             mid = left + (right - left) // 2
#             num_of_ribbon = 0

#             for i in ribbons:
#                 num_of_ribbon += i // mid

#             if num_of_ribbon >= k:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return right
    
    
        def count_ribbon(n):
            num_of_ribbon = 0
            for r in ribbons:
                num_of_ribbon += r // n
            return num_of_ribbon

        left = 1
        right = sum(ribbons) // k+1

        while left < right:
            mid = left + (right - left) // 2

            if count_ribbon(mid) < k:
                right = mid
            else:
                left = mid + 1

        return left - 1