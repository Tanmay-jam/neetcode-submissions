# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=curr=ListNode(next=head)
        for i in range(left):
            prev = curr
            curr = curr.next
        start = prev
        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        start.next.next = curr
        start.next = prev
        return dummy.next