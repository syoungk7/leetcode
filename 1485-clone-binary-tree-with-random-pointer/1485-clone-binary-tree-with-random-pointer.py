# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def dfs(original_node, copies):
            if not original_node:
                return None

            if original_node in copies:
                return copies[original_node]

            new_node = NodeCopy(original_node.val)
            copies[original_node] = new_node

            new_node.left = dfs(original_node.left, copies)
            new_node.right = dfs(original_node.right, copies)
            new_node.random = dfs(original_node.random, copies)

            return new_node

        copies = {}
        return dfs(root, copies)