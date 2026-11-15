# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        from collections import deque
        q = deque([root])
        dq = deque()
        depth = 0
        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                if depth%2:
                    dq.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            while dq:
                start, end = dq.popleft(), dq.pop()
                start.val, end.val = end.val, start.val
            depth+=1
        return root

                