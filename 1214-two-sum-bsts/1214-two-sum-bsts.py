# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        self.ans = False # from other's solutions
        root1_dic = {} # dic is faster than list no need to call the list in def

        # from solution
        def dfs(node):
            if not node: return
            root1_dic[node.val] = 1
            dfs(node.left)
            dfs(node.right)

            
        def dfs_2(node):
            if not node: return
            if target - node.val in root1_dic: 
                self.ans=True
                
                return
            dfs_2(node.left)
            dfs_2(node.right)

        dfs(root1)
        dfs_2(root2)
        
        return self.ans