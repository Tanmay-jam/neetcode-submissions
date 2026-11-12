# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rsum=0
        def dfs(node, low, high):
            if not node:
                return 0
            if node.val<low:
                return dfs(node.right, low, high)
            if node.val>high:
                return dfs(node.left, low, high)
            return node.val + dfs(node.left, low, high) + dfs(node.right, low, high)
        return dfs(root, low, high)