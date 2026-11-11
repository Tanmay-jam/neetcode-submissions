# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        curr = TreeNode()
        if not root1 or not root2:
            curr.val = root1.val if root1 else root2.val
        else:
            curr.val = root1.val+root2.val
        curr.left = self.mergeTrees(root1.left if root1 else root1, root2.left if root2 else root2)
        curr.right = self.mergeTrees(root1.right if root1 else root1, root2.right if root2 else root2)
        return curr