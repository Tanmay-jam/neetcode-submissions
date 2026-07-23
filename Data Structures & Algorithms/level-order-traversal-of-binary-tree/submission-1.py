# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        trav =  []

        from collections import deque
        q = deque()
        q.append(root)
        while q:
            temp=[]
            le = len(q)
            for i in range(le):
                node = q.popleft()
                temp.append(node.val)
                q.append(node.left) if node.left else 1==1
                q.append(node.right) if node.right else 1==1
            trav.append(temp)
        return trav