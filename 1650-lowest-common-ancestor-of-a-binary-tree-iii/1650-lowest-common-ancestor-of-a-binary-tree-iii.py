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
        tmp = set()
        
        def recur_ances(node):
            if node is None or node in tmp:
                return node
            else:
                tmp.add(node)
                node = node.parent
                return recur_ances(node)

        return recur_ances(p) or recur_ances(q)

#         p1, p2 = p, q
#         while p1 != p2:
#             p1 = p1.parent if p1.parent else q
#             p2 = p2.parent if p2.parent else p
            
#         return p1