# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same(self, t1, t2):
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        if t1.val != t2.val:
            return False
        return self.same(t1.left, t2.left) and self.same(t1.right, t2.right) and True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(node):
            if not node:
                return
            nonlocal res
            if self.same(node, subRoot):
                res = True
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
        