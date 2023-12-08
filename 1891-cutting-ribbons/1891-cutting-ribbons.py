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
    
    
        n = len(ribbons)
        l, r = 1, max(ribbons)

        def could(ribbons, length, k):
            count = 0
            for r in ribbons:
                count += r//length
                if count >= k: return True
            return count >= k
        
        while l <= r:
            m = l + (r-l)//2
            if could(ribbons, m, k):
                l = m+1
            else:
                r = m-1
        if r <= 0: return 0
        return r