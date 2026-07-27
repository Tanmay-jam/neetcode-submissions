# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root==None:
            return ans
        from collections import deque
        q = deque([root])
        while q:
            l = len(q)
            cnt=0
            for i in range(len(q)):
                if cnt==0:
                    ans.append(q[-1].val)
                    cnt+=1
                node = q.popleft()
                q.append(node.left) if node.left else 1==1
                q.append(node.right) if node.right else 1==1
        return ans