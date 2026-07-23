# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self, n1, n2):
        if n1==None and n2==None:
            return True
        elif n1==None or n2==None:
            return False
        
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        t1, t2 = '',''
        def preorder(node, t):
            if not node:
                t+=',N'
                return t
            t+= ','+str(node.val)
            t = preorder(node.left, t)
            t = preorder(node.right, t)
            return t
        t1 = preorder(root, t1)
        t2 = preorder(subRoot, t2)

        return t2 in t1

        