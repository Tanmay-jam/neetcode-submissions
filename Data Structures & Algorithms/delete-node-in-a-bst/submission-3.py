# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            replace = root.right
            prev=root
            while replace.left:
                prev=replace
                replace=replace.left
            root.val = replace.val
            if prev==root:
                prev.right=replace.right
            else:
                prev.left=replace.right
            return root
        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        return root