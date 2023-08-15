"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        longest = 0
        
        def depth_calculation(node, depth):
            nonlocal longest
            
            if not node.children: return depth
            new, old = depth, 0

            for child in node.children:
                update = depth_calculation(child, depth+1)
                
                if update > new: new, old = update, new
                elif update > old: old = update

            dist = new + old - 2 * depth
            longest = max(longest, dist)

            return new
        
        depth_calculation(root, 0)
        return longest