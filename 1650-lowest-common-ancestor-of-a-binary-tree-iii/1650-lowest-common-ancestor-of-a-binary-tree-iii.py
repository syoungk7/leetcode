"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        seen = set()
        target = p

        while target:
            seen.add(target)
            target = target.parent
        target = q

        while not target in seen:
            target = target.parent
        return target

#         left, right = p, q
#         while left != right:
#             if left.parent:
#                 left = left.parent
#             else: left = q
            
#             if right.parent:
#                 right = right.parent 
#             else: right = p
            
#         return left