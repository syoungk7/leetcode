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
            else:
                new = NodeCopy(o_node.val)
                cp[o_node] = new

            new.left = dfs(o_node.left, cp)
            new.right = dfs(o_node.right, cp)
            new.random = dfs(o_node.random, cp)
            return new
        
        return dfs(root, cp)
    
## ref solution

# Recursive DFS

#     def __init__(self):
#         # track visited nodes to avoid cycles
#         self.visited = dict()

#     def copyRandomBinaryTree(self, root: "Node") -> "NodeCopy":
#         if not root: return

#         # check if already created and return
#         if root in self.visited: return self.visited[root]

#         # otherwise, create a node and remember to save it in visited
#         node = NodeCopy(root.val, None, None, None)
#         self.visited[root] = node

#         # recurse on other pointers
#         node.left = self.copyRandomBinaryTree(root.left)
#         node.right = self.copyRandomBinaryTree(root.right)
#         node.random = self.copyRandomBinaryTree(root.random)

#         return node

# Iterative DFS

#     def copyRandomBinaryTree(self, root: "Node") -> "NodeCopy":
#         if not root: return

#         # track visited nodes to avoid cycles
#         visited = collections.defaultdict(lambda: NodeCopy())
#         visited[None] = None
#         S = [root]

#         while S:
#             node = S.pop()

#             # create old_node to new_node reference
#             visited[node].val = node.val
#             visited[node].left = visited[node.left]
#             visited[node].right = visited[node.right]
#             visited[node].random = visited[node.random]

#             # explore children
#             for child in (node.left, node.right):
#                 if child: S.append(child)

#         return visited[root]