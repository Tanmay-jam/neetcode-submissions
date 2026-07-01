# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1, t2 = [], []

        def dfs(node, t):
            if node==None:
                t.append(None)
                return
            t.append(node.val)
            dfs(node.left, t)
            dfs(node.right, t)
            return t
        
        t1 = dfs(p, t1)
        t2 = dfs(q, t2)

        return t1==t2