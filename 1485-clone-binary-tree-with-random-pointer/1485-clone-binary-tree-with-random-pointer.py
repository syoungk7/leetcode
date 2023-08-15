# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        cp = {}

        def dfs(o_node, cp):
            if not o_node: return None
            if o_node in cp: return cp[o_node]

            new = NodeCopy(o_node.val)
            cp[o_node] = new

            new.left = dfs(o_node.left, cp)
            new.right = dfs(o_node.right, cp)
            new.random = dfs(o_node.random, cp)
            return new
        
        return dfs(root, cp)