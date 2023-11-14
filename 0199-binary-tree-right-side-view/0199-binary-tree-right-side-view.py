# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        self.out = []
        level = 0
        def recur_right(root, level):
            if level == len(self.out):
                self.out.append(root.val)
            
            for i in [root.right, root.left]:
                if i:
                    recur_right(i, level+1)

                
        recur_right(root, level)
        return self.out