# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.ans=False
        
        # from solution
        def dfs(curr_node, node_list):
            if not curr_node:
                return
            node_list.append(curr_node.val)
            dfs(curr_node.left, node_list)
            dfs(curr_node.right, node_list)
            
        def dfs_2(curr_node):
            if not curr_node:
                return
            print(curr_node.val)
            if curr_node.val in sub_lst:
                self.ans=True
            dfs_2(curr_node.left)
            dfs_2(curr_node.right)

        root1_lst, sub_lst = [], []
        dfs(root1, root1_lst)
        for i in root1_lst:
            sub_lst.append(target-i)
        print(sub_lst)
        
        dfs_2(root2)
        
        return self.ans 