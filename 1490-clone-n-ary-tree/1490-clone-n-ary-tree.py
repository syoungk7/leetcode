"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None
        new = Node()

        def dfs(root, new):
            if not root: return None

            new.val = root.val

            for child in root.children:
                cp = Node()
                new.children.append(cp)
                dfs(child, cp)
            
        dfs(root, new)
        return new

# ??
#        return deepcopy(root)