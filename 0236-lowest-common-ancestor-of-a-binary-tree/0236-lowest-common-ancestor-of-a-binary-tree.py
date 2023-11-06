# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root == p or root == q:
#             return root
        
#         left = right = None
#         if root.left:
#             left = self.lowestCommonAncestor(root.left, p, q)
#         if root.right:
#             right = self.lowestCommonAncestor(root.right, p, q)

#         if left and right:
#             return root
#         elif left:
#             return left
#         else:
#             return right


        parent = {root: None}
        que = [root]

        while not (p in parent and q in parent):
            node = que.pop()
            if node.left:
                parent[node.left] = node
                que.append(node.left)
            if node.right:
                parent[node.right] = node
                que.append(node.right)
            
        ancestors = {p}
        while parent[p]:
            ancestors.add(parent[p])
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q
            