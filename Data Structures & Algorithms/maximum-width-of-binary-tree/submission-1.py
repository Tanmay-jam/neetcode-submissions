# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([(root, 0)])
        maxWidth=0
        while q:
            start = q[0][1]
            l=len(q)
            for _ in range(l):
                node, num = q.popleft()
                curNum = num - start
                maxWidth = max(maxWidth, curNum)
                if node.left:
                    q.append((node.left, 2*curNum))
                if node.right:
                    q.append((node.right, 2*curNum+1))
        return maxWidth + 1
        