# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        from collections import deque
        q=deque([(root, root.val)])
        levelSum=root.val
        while q:
            l = len(q)
            nextLevelSum=0
            for _ in range(l):
                treeNode = q.popleft()
                node, sibSum = treeNode[0], treeNode[1]
                node.val = levelSum - sibSum
                nextSiblingSum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    q.append([node.left, nextSiblingSum])
                    nextLevelSum+=node.left.val
                if node.right:
                    q.append([node.right, nextSiblingSum])
                    nextLevelSum+=node.right.val
            levelSum=nextLevelSum
        return root
