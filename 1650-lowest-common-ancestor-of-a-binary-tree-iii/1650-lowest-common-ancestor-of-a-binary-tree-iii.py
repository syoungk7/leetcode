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
#         tmp = set()
        
#         def recur_ances(node):
#             if node is None or node in tmp:
#                 return node
#             else:
#                 tmp.add(node)
#                 node = node.parent
#                 return recur_ances(node)

#         return recur_ances(p) or recur_ances(q)

        left, right = p, q
        while left != right:
            if left.parent:
                left = left.parent
            else: left = q
            
            if right.parent:
                right = right.parent 
            else: right = p
            
        return left