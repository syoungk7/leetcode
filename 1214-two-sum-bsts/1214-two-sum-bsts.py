# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.ans=False
        root1_lst = {}

        # from solution
        def dfs(node, node_list):
            if not node: return
            node_list[node.val] = 1
            dfs(node.left, node_list)
            dfs(node.right, node_list)
            
        def dfs_2(node):
            if not node: return
            print(target - node.val)
            if target - node.val in root1_lst:
                self.ans=True
            dfs_2(node.left)
            dfs_2(node.right)

        dfs(root1, root1_lst)
        dfs_2(root2)
        
        return self.ans 