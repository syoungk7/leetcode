# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # from solution
        def dfs(curr_node, node_list):
            if not curr_node:
                return
            node_list.append(curr_node.val)
            dfs(curr_node.left, node_list)
            dfs(curr_node.right, node_list)
        
        root1_lst, root2_lst = [], []
        dfs(root1, root1_lst)
        dfs(root2, root2_lst)
        
        a = [True for i in root1_lst for j in root2_lst if i+j == target]
        return a
        