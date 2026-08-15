# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        elif key>root.val:
            root.right = self.deleteNode(root.right, key)
        elif key==root.val:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            end1, start2 = root.left, root.right
            while end1.right:
                end1 = end1.right
            end1.right = start2
            return root.left
        return root
            