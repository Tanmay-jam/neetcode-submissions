class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def func(l, h):
            if l>h:
                return
            mid = (l+h)//2
            curr = TreeNode(nums[mid])
            curr.left = func(l, mid-1)
            curr.right = func(mid+1, h)
            return curr
        return func(0, len(nums)-1)