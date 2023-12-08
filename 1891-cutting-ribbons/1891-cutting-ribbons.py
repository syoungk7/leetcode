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
    
    
        def f(n):
            ans = 0
            for ribbon in ribbons:
                ans += ribbon//n
            return ans

        l = 1
        r = sum(ribbons)//k+1

        while l < r:
            mid = l + (r-l)//2

            if f(mid) < k:
                r = mid
            else:
                l = mid+1

        return l-1