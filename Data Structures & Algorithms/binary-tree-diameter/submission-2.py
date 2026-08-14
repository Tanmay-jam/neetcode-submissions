# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def dfs(node):
            if not node:
                return 0
            nonlocal dia
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            dia = max(dia, left_height+right_height)
            return max(left_height, right_height) + 1
        dfs(root)
        return dia